"""python3 main.py로 실행하세요."""
from game import QuizGame


def main():
    game = None
    try:
        game = QuizGame()
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 안전하게 종료합니다. 미완료 게임과 등록 중인 문제는 반영하지 않습니다.")
    finally:
        if game is not None:
            if game.save():
                print("데이터를 저장했습니다. 다음에 또 만나요!")


if __name__ == "__main__":
    main()
