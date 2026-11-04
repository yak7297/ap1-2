"""모든 메뉴에서 함께 사용하는 입력 처리."""


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("빈 입력은 사용할 수 없습니다. 다시 입력하세요.")


def read_number(prompt, minimum, maximum):
    while True:
        value = read_text(prompt)
        try:
            number = int(value)
        except ValueError:
            print("숫자를 입력하세요.")
            continue
        if minimum <= number <= maximum:
            return number
        print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")
