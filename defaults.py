"""직접 작성한 Python 기초 문제 5개."""
from quiz import Quiz


def default_quizzes():
    return [
        Quiz("Python에서 정수를 나타내는 자료형은?", ["str", "int", "list", "dict"], 2),
        Quiz("리스트 끝에 항목을 추가하는 메서드는?", ["append()", "pop()", "clear()", "keys()"], 1),
        Quiz("조건에 따라 실행할 코드를 나누는 키워드는?", ["for", "import", "if", "def"], 3),
        Quiz("함수를 정의할 때 사용하는 키워드는?", ["class", "return", "while", "def"], 4),
        Quiz("키와 값의 쌍을 저장하는 자료형은?", ["bool", "list", "dict", "str"], 3),
    ]
