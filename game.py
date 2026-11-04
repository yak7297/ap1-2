"""메뉴와 게임 진행을 담당합니다."""
from inputs import read_number, read_text


class QuizGame:
    def __init__(self):
        self.quizzes = []
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
        print("준비 중입니다.")

    def add_quiz(self):
        print("준비 중입니다.")

    def list_quizzes(self):
        print("준비 중입니다.")

    def show_score(self):
        print("준비 중입니다.")
