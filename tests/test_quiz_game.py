"""실제 state.json을 건드리지 않는 표준 라이브러리 테스트."""
import contextlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from game import QuizGame
from inputs import read_number
from storage import StateStore

ROOT = Path(__file__).resolve().parents[1]


class QuizGameTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'state.json'
        self.output = io.StringIO()
        self.capture = contextlib.redirect_stdout(self.output)
        self.capture.__enter__()
        self.addCleanup(self.capture.__exit__, None, None, None)

    def game(self):
        return QuizGame(StateStore(self.path))

    def test_missing_file_uses_five_quizzes(self):
        self.assertEqual(len(self.game().quizzes), 5)

    def test_numeric_input_retries_blank_text_and_out_of_range(self):
        with patch('builtins.input', side_effect=['', 'abc', '0', '9', ' 2 ']):
            self.assertEqual(read_number('선택: ', 1, 5), 2)
        self.assertIn('빈 입력', self.output.getvalue())
        self.assertIn('숫자를 입력', self.output.getvalue())
        self.assertIn('1~5', self.output.getvalue())

    def test_add_and_reload_unicode_quiz(self):
        game = self.game()
        with patch('builtins.input', side_effect=['', '  한글 문제  ', '가', '나', '다', '라', 'x', '0', ' 2 ']):
            game.add_quiz()
        loaded = self.game()
        self.assertEqual(len(loaded.quizzes), 6)
        self.assertEqual(loaded.quizzes[-1].question, '한글 문제')
        self.assertEqual(loaded.quizzes[-1].answer, 2)
        self.assertIn('한글 문제', self.path.read_text(encoding='utf-8'))

    def test_play_saves_best_and_lower_score_does_not_replace_it(self):
        game = self.game()
        original_order = game.quizzes.copy()
        # 결정적인 역순 출제로 원본 보존과 섞인 문제의 정답 판정을 함께 확인합니다.
        with patch('game.random.shuffle', side_effect=lambda items: items.reverse()) as shuffle:
            with patch('builtins.input', side_effect=[str(q.answer) for q in reversed(game.quizzes)]):
                game.play()
        shuffle.assert_called_once()
        self.assertEqual(game.quizzes, original_order)
        reloaded = self.game()
        self.assertEqual(reloaded.best_score, 100)
        with patch('game.random.shuffle'), patch('builtins.input', side_effect=['1'] * 5):
            reloaded.play()
        self.assertEqual(self.game().best_score, 100)
        self.assertIn('오답입니다', self.output.getvalue())

    def test_first_play_zero_is_a_played_score(self):
        game = self.game()
        wrong = [str(q.answer % 4 + 1) for q in game.quizzes]
        with patch('game.random.shuffle'), patch('builtins.input', side_effect=wrong):
            game.play()
        loaded = self.game()
        self.assertTrue(loaded.played)
        self.assertEqual(loaded.best_score, 0)
        loaded.show_score()
        self.assertIn('최고 점수: 0점', self.output.getvalue())

    def test_empty_quiz_list_is_valid(self):
        game = self.game()
        game.quizzes = []
        game.save()
        loaded = self.game()
        self.assertEqual(loaded.quizzes, [])
        loaded.play()
        loaded.list_quizzes()
        self.assertIn('등록된 퀴즈가 없습니다', self.output.getvalue())

    def test_no_play_yet_message(self):
        self.game().show_score()
        self.assertIn('아직 퀴즈를 풀지', self.output.getvalue())

    def test_corrupt_json_and_schema_recover(self):
        for broken in ['{bad', '[]', '{"quizzes": [42]}',
                       '{"quizzes": [], "best_score": true, "played": false, "best_correct": 0, "best_total": 0}']:
            with self.subTest(broken=broken):
                self.path.write_text(broken, encoding='utf-8')
                self.assertEqual(len(self.game().quizzes), 5)
        self.assertEqual(len(list(self.path.parent.glob('state.corrupt-*.json'))), 4)

    def test_invalid_utf8_recovers(self):
        self.path.write_bytes(b'\xff\xfe')
        self.assertEqual(len(self.game().quizzes), 5)

    def test_read_error_and_write_error_are_reported(self):
        self.path.mkdir()
        game = self.game()
        self.assertFalse(game.save())
        self.assertIn('파일 읽기 실패', self.output.getvalue())
        self.assertIn('저장 실패', self.output.getvalue())

    def test_interrupted_add_does_not_append_partial_quiz(self):
        game = self.game()
        with patch('builtins.input', side_effect=['미완료 문제', KeyboardInterrupt]):
            with self.assertRaises(KeyboardInterrupt):
                game.add_quiz()
        self.assertEqual(len(game.quizzes), 5)

    def test_interrupted_play_keeps_existing_score(self):
        game = self.game()
        with patch('builtins.input', side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                game.play()
        self.assertFalse(game.played)
        self.assertEqual(game.best_score, 0)

    def test_main_keyboardinterrupt_safely_saves(self):
        import main
        game = self.game()
        with patch('main.QuizGame', return_value=game), patch('builtins.input', side_effect=KeyboardInterrupt):
            main.main()
        self.assertTrue(self.path.exists())
        self.assertIn('안전하게 종료', self.output.getvalue())

    def test_real_process_restarts_and_handles_eof_from_other_directory(self):
        project = Path(self.temp.name) / 'project'
        project.mkdir()
        for file in ROOT.glob('*.py'):
            shutil.copy(file, project / file.name)
        command = [sys.executable, str(project / 'main.py')]
        first = subprocess.run(command, input='2\n테스트 문제\n하나\n둘\n셋\n넷\n1\n5\n', text=True, capture_output=True, cwd=self.temp.name)
        self.assertEqual(first.returncode, 0, first.stderr)
        second = subprocess.run(command, input='3\n4\n', text=True, capture_output=True, cwd=self.temp.name)
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertIn('테스트 문제', second.stdout)
        self.assertIn('안전하게 종료', second.stdout)
        self.assertEqual(len(json.loads((project / 'state.json').read_text())['quizzes']), 6)
        self.assertFalse(self.path.exists())  # 현재 작업 위치 대신 프로젝트 루트에 저장


if __name__ == '__main__':
    unittest.main()
