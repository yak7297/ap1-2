"""메뉴와 게임 진행을 담당합니다."""
from defaults import default_quizzes
from quiz import Quiz
from inputs import read_number, read_text


class QuizGame:
    def __init__(self):
        self.quizzes = default_quizzes()
        self.best_score = 0
        self.played = False

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
        # SCORE_UPDATE

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")
        question = read_text("문제: ")
        choices = [read_text(f"선택지 {index}: ") for index in range(1, 5)]
        answer = read_number("정답 번호 (1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다.")
        # SAVE_ADDED

    def list_quizzes(self):
        print("준비 중입니다.")

    def show_score(self):
        print("준비 중입니다.")
