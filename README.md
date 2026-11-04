# Python 기초 퀴즈 게임

Python 3.10 이상과 표준 라이브러리만 사용하는 콘솔 프로그램입니다. 퀴즈를 풀고, 직접 문제를 추가하고, 목록과 최고 점수를 확인할 수 있습니다. 보너스는 **랜덤 출제** 하나를 구현했습니다.

## 주제와 선정 이유

주제는 **Python 기초 문법**입니다. 자료형, 리스트, 조건문, 함수, 딕셔너리를 퀴즈로 복습하면서 이 프로그램에 쓰인 문법도 함께 이해할 수 있어 선정했습니다. 직접 작성한 기본 문제 5개가 포함됩니다.

## 실행 방법 (macOS / VS Code)

1. VS Code에서 이 README가 들어 있는 `python-quiz-game` 폴더를 엽니다.
2. 상단 메뉴 **터미널 → 새 터미널**을 엽니다.
3. 아래 명령을 입력합니다. 별도 패키지 설치는 필요 없습니다.

```sh
python3 --version
python3 main.py
```

Python 버전이 3.10 이상이어야 합니다. Windows에서 `python3` 명령이 없다면 `python main.py`를 사용합니다.

메뉴에서 1~5를 선택합니다.

```text
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
```

## 기능 목록

| 기능 | 동작 |
| --- | --- |
| 퀴즈 풀기 | 등록된 모든 문제 출제, 정답/오답 안내, 최종 점수 출력 |
| 퀴즈 추가 | 문제, 선택지 4개, 정답 번호 1~4 입력 후 즉시 저장 |
| 퀴즈 목록 | 등록된 문제 제목과 번호 표시 |
| 점수 확인 | 최고 점수와 당시 전체 문제 수/정답 수 표시 |
| 종료 | 데이터 저장 후 종료 |
| 보너스: 랜덤 출제 | 매 게임 `random.shuffle()`로 복사한 문제 목록을 섞음 |

빈 입력, 문자, 범위 밖 숫자는 안내 후 다시 입력받습니다. 앞뒤 공백은 제거합니다. Ctrl+C 또는 입력 스트림 종료 시 안내 후 완료된 데이터만 저장합니다. 등록 중인 문제와 풀다 중단한 게임 결과는 반영하지 않습니다. 문제 목록이 비었거나 아직 플레이하지 않은 경우 별도로 안내합니다.

점수는 `round(정답 수 / 전체 문제 수 * 100)`으로 계산합니다. 최고 점수를 갱신할 때 당시 정답 수와 전체 문제 수도 함께 저장합니다. 최고 점수와 동점이면 기존 기록을 유지합니다. 0점으로 완료한 게임도 플레이 이력으로 인정합니다. 랜덤 출제는 우연히 이전과 같은 순서가 나올 수 있습니다.

## 파일 구조

```text
python-quiz-game/
├── main.py                 # 시작, Ctrl+C/EOF 처리, 종료 시 저장
├── game.py                 # QuizGame: 메뉴, 플레이, 등록, 목록, 점수
├── quiz.py                 # Quiz: 문제, 선택지, 정답, 출력 및 판정
├── defaults.py             # 직접 작성한 기본 퀴즈 5개
├── inputs.py               # 문자열/숫자 입력 검증
├── storage.py              # StateStore: JSON 저장, 불러오기, 복구
├── state.json              # 퀴즈와 최고 점수 (프로젝트 루트)
├── tests/test_quiz_game.py  # 표준 unittest 테스트
├── docs/
│   ├── LEARNING.md         # 코드 설명과 학습 정리
│   ├── SUBMISSION.md       # GitHub 업로드와 제출 체크리스트
│   ├── evidence/           # 실제 테스트 및 실행 로그
│   └── screenshots/README.md # 직접 캡처할 화면 안내
├── .gitignore
└── README.md
```

## 데이터 파일 설명

`state.json`은 현재 터미널 위치와 관계없이 **프로그램 파일이 있는 프로젝트 루트**에 저장됩니다. UTF-8과 `ensure_ascii=False`로 한글을 읽을 수 있게 저장합니다. 제출용 초기 파일에는 문제 5개와 미플레이 상태가 담겨 있습니다.

데이터 형식 예시 (실제 파일에는 기본 문제 5개가 포함됨):

```json
{
  "quizzes": [
    {
      "question": "Python에서 정수를 나타내는 자료형은?",
      "choices": ["str", "int", "list", "dict"],
      "answer": 2
    }
  ],
  "best_score": 0,
  "played": false,
  "best_correct": 0,
  "best_total": 0
}
```

- `quizzes`: 등록된 퀴즈 배열. 각 항목은 문제, 문자열 선택지 4개, 정답 번호 1~4를 가집니다.
- `best_score`: 0~100의 최고 점수 정수.
- `played`: 끝까지 완료한 게임이 있으면 `true`.
- `best_correct`, `best_total`: 최고 점수 당시 정답 수와 문제 수.

파일이 없으면 기본 퀴즈를 사용합니다. JSON 형식, 필수 필드, 자료형, 점수와 정답 수 일치 여부를 검증합니다. 파일이 손상되면 안내 후 `state.corrupt-날짜-시각.json`에 원본 백업을 시도하고 기본 데이터로 복구합니다. 읽기/쓰기 오류는 메시지로 알려줍니다. 저장은 임시 파일 작성 후 교체하여 저장 도중 기존 파일이 잘리는 위험을 줄입니다.

## 검증

```sh
python3 -m unittest discover -s tests -v
```

14개 테스트를 통과했습니다. 별도 임시 폴더에서 실행하므로 제출용 `state.json`을 변경하지 않습니다. 실제 결과는 `docs/evidence/tests.txt`, 실제 콘솔 실행 출력은 `docs/evidence/console-session.txt`와 `restart-session.txt`에 있습니다. 자동 검증 로그는 화면 캡처와 별개입니다.

## Git 기록과 제출 상태

기능별 커밋 10개 이상과 `feature/quiz-play` 브랜치 생성 및 `main`으로의 병합 기록이 포함되어 있습니다.

```sh
git log --oneline --graph --all
git rev-list --count HEAD
```

**GitHub 저장소 생성/업로드, 원격 clone → 변경 → commit → push → 기존 폴더 pull 실습, 제출용 실제 화면 캡처는 아직 완료되지 않았습니다.** 정확한 절차는 `docs/SUBMISSION.md`에 있습니다. 폴더를 복사할 때 숨김 폴더 `.git`도 유지해야 기존 커밋과 병합 기록을 보존할 수 있습니다. 소스 코드 ZIP만 GitHub에 올리면 커밋 기록은 전달되지 않습니다.
