"""프로젝트 루트 state.json의 UTF-8 저장과 복구."""
import json
from datetime import datetime
from pathlib import Path
from defaults import default_quizzes
from quiz import Quiz

STATE_PATH = Path(__file__).resolve().parent / "state.json"


class StateStore:
    def __init__(self, path=STATE_PATH):
        self.path = Path(path)

    def default_state(self):
        return {"quizzes": default_quizzes(), "best_score": 0,
                "played": False, "best_correct": 0, "best_total": 0}

    def load(self):
        if not self.path.exists():
            print("첫 실행입니다. 기본 퀴즈 5개를 사용합니다.")
            return self.default_state()
        try:
            with self.path.open(encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, dict) or not isinstance(data["quizzes"], list):
                raise ValueError("퀴즈 목록 형식 오류")
            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            score, played = data["best_score"], data["played"]
            correct, total = data["best_correct"], data["best_total"]
            if type(score) is not int or not 0 <= score <= 100 or type(played) is not bool:
                raise ValueError("점수 형식 오류")
            if type(correct) is not int or type(total) is not int or not 0 <= correct <= total:
                raise ValueError("정답 수 형식 오류")
            if played and (total == 0 or score != round(correct / total * 100)):
                raise ValueError("점수와 정답 수 불일치")
            if not played and (score != 0 or correct != 0 or total != 0):
                raise ValueError("미플레이 상태의 점수 오류")
            print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고점수 {score}점)")
            return dict(quizzes=quizzes, best_score=score, played=played,
                        best_correct=correct, best_total=total)
        except (ValueError, KeyError, TypeError, UnicodeError) as error:
            print(f"데이터가 손상되었습니다: {error}. 기본 퀴즈로 복구합니다.")
            backup = self.path.with_name("state.corrupt-" + datetime.now().strftime("%Y%m%d-%H%M%S-%f") + ".json")
            try:
                self.path.replace(backup)
                print(f"손상 파일 백업: {backup.name}")
            except OSError as backup_error:
                print(f"백업 실패: {backup_error}")
            return self.default_state()
        except OSError as error:
            print(f"파일 읽기 실패: {error}. 기본 퀴즈를 사용합니다.")
            return self.default_state()

    def save(self, state):
        data = dict(state)
        data["quizzes"] = [quiz.to_dict() for quiz in state["quizzes"]]
        temporary = self.path.with_suffix(".json.tmp")
        try:
            with temporary.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
                file.write("\n")
            temporary.replace(self.path)
            return True
        except OSError as error:
            print(f"저장 실패: {error}. 이번 변경은 재실행 시 유지되지 않을 수 있습니다.")
            return False
