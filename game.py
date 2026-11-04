"""메뉴와 게임 진행을 담당합니다."""
from defaults import default_quizzes
from quiz import Quiz
from inputs import read_number, read_text


class QuizGame:
    def __init__(self):
        self.quizzes = default_quizzes()
        self.best_score = 0
        self.played = False
        self.best_correct = 0
        self.best_total = 0

    def show_menu(self):
        print("\n" + "=" * 40)
        print("        Python 기초 퀴즈 게임")
        print("=" * 40)
        print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")

    def run(self):
        while True:
            self.show_menu()
            choice = read_number("선택: ", 1, 5)
            if choice == 1:
                self.play()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            else:
                print("게임을 종료합니다.")
                break

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return
        questions = self.quizzes.copy()
        correct = 0
        print(f"\n퀴즈를 시작합니다! 총 {len(questions)}문제")
        for index, quiz in enumerate(questions, start=1):
            quiz.display(index)
            answer = read_number("정답 번호 (1~4): ", 1, 4)
            if quiz.is_correct(answer):
                correct += 1
                print("정답입니다!")
            else:
                print(f"오답입니다. 정답: {quiz.answer}. {quiz.choices[quiz.answer - 1]}")
        score = round(correct / len(questions) * 100)
        print(f"\n결과: {len(questions)}문제 중 {correct}문제 정답! ({score}점)")
        if not self.played or score > self.best_score:
            self.best_score = score
            self.best_correct = correct
            self.best_total = len(questions)
            print("새로운 최고 점수입니다!")
        self.played = True
        # SAVE_SCORE

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")
        question = read_text("문제: ")
        choices = [read_text(f"선택지 {index}: ") for index in range(1, 5)]
        answer = read_number("정답 번호 (1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다.")
        # SAVE_ADDED

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")

    def show_score(self):
        if not self.played:
            print("아직 퀴즈를 풀지 않았습니다.")
            return
        print(f"최고 점수: {self.best_score}점 ({self.best_total}문제 중 {self.best_correct}문제 정답)")
