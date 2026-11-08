# Python 기초 퀴즈 게임

Python 3.10 이상과 표준 라이브러리만 사용하는 콘솔 프로그램입니다. 퀴즈를 풀고, 직접 문제를 추가하고, 목록과 최고 점수를 확인할 수 있습니다. 보너스는 **랜덤 출제** 하나를 구현했습니다.

## 설계 및 학습 설명

- [커밋 메시지 규칙과 기능별 커밋 단위 — 평가 #12](docs/LEARNING.md#commit-convention)
- [Quiz/QuizGame 클래스 사용 이유와 함수 중심 구현 비교 — 평가 #13](docs/LEARNING.md#class-design)
- [JSON 선택 이유, 대용량·빈번한 쓰기·동시 저장의 한계와 대안 — 평가 #18](docs/LEARNING.md#json-tradeoffs)
- [메뉴와 기능별 주요 출력 모음](docs/USAGE.md)
- [스크린샷 파일명·캡처 시각 목록](docs/screenshots/README.md)

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

오답이면 `오답입니다. 정답: 번호. 선택지` 형식으로 올바른 답을 알려주고 정답 수를 늘리지 않습니다. 별도의 감점은 없습니다.

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
│   ├── LEARNING.md         # 설계 이유, 커밋 규칙, JSON 한계와 학습 정리
│   ├── USAGE.md            # 메뉴와 기능별 주요 출력 예시
│   ├── SUBMISSION.md       # GitHub 업로드와 제출 체크리스트
│   ├── evidence/           # 실제 테스트 및 실행 로그
│   └── screenshots/          # 사용자가 직접 캡처한 실제 실행 이미지
├── .gitignore
└── README.md
```

## 데이터 파일 설명

`state.json`은 현재 터미널 위치와 관계없이 **프로그램 파일이 있는 프로젝트 루트**에 저장됩니다. UTF-8과 `ensure_ascii=False`로 한글을 읽을 수 있게 저장합니다. 기본 문제는 5개입니다. 현재 로컬 파일에는 사용자 실습에서 추가한 문제까지 총 6개와 최고 점수 33점이 저장되어 있습니다. 저장 파일이 없을 때는 기본 5문제로 시작합니다.

데이터 형식 예시 (구조 설명을 위한 미플레이 상태):

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

### 저장 시점과 중단 처리

- `QuizGame.add_quiz()`에서 문제·선택지·정답을 모두 입력하고 등록한 직후 저장합니다.
- `QuizGame.play()`에서 모든 문제를 풀고 최고 점수와 플레이 상태를 갱신한 직후 저장합니다. 최고 점수를 갱신하지 않아도 저장합니다.
- 정상 종료, Ctrl+C, EOF 시 `main.main()`의 `finally`에서 현재 완료된 상태를 다시 저장합니다. 입력 중이던 문제는 목록에 추가되지 않고, 풀다 중단한 게임은 점수에 반영되지 않습니다.
- 메뉴 표시, 목록 보기, 점수 확인만으로는 직접 파일을 쓰지 않습니다. 첫 실행·손상 복구 직후 기본 데이터는 메모리에 준비되며 위 저장 시점에 파일에 기록됩니다.

`STATE_PATH`는 `Path(__file__).resolve().parent / "state.json"`으로 계산한 절대경로입니다. 터미널의 상대경로 위치를 바꿔 실행해도 같은 프로젝트 루트에 저장합니다.

JSON은 사람이 읽을 수 있고 표준 라이브러리만으로 처리할 수 있어 선택했습니다. 전체 읽기·재저장 방식이라 대용량과 빈번한 쓰기에 한계가 있고 동시 실행 충돌을 막지 못합니다. [한계와 대안, 스키마 변경 시 호환성](docs/LEARNING.md#json-tradeoffs)에 정리했습니다.

손상 복구 시 프로젝트 루트의 `state.corrupt-날짜-시각.json`으로 원본 이동을 시도하고 백업 파일명을 터미널에 알립니다. 백업 또는 읽기/쓰기 실패 원인도 화면에 출력합니다. 상세 오류를 별도 로그 파일에 자동으로 누적하는 기능은 현재 없습니다. 원인을 확인할 때 안내 문구와 백업 파일을 함께 보관합니다.

## 검증

```sh
python3 -m unittest discover -s tests -v
```

14개 테스트를 통과했습니다. 별도 임시 폴더에서 실행하므로 제출용 `state.json`을 변경하지 않습니다. 실제 결과는 `docs/evidence/tests.txt`, 실제 콘솔 실행 출력은 `docs/evidence/console-session.txt`와 `restart-session.txt`에 있습니다. 자동 검증 로그는 화면 캡처와 별개입니다.

## Git 기록과 제출 상태

기능별 커밋 10개 이상과 `feature/quiz-play` 브랜치 생성 및 `main`으로의 병합 기록이 포함되어 있습니다. 메시지는 `프리픽스: 변경 요약` 형식이며, 메뉴·모델·플레이·등록·점수·저장 등 설명 가능한 기능 단위로 나눕니다. [전체 커밋 규칙과 브랜치 전략](docs/LEARNING.md#commit-convention)에 예시를 정리했습니다.

```sh
git log --oneline --graph --all
git rev-list --count HEAD
```

GitHub 제출 대상은 [yak7297/ap1-2](https://github.com/yak7297/ap1-2)입니다. 실행 캡처 8개, 개발 환경과 Git 그래프 각 1개, Git 업로드와 복제 실습 캡처 4개로 총 14개를 포함했습니다. main과 기능 브랜치 업로드, 원격 clone → README 수정 → commit → push → 원래 폴더 pull 실습을 완료했습니다. 제출 점검표는 `docs/SUBMISSION.md`에 있습니다. 폴더를 복사할 때 숨김 폴더 `.git`도 유지해야 기존 커밋과 병합 기록을 보존할 수 있습니다. 소스 코드 ZIP만 GitHub에 올리면 커밋 기록은 전달되지 않습니다.


## 실제 실행 화면

사용자가 2026-11-04에 VS Code 터미널에서 직접 실행하고 캡처한 화면입니다.

### 메뉴
![메뉴 실행 화면](docs/screenshots/menu.png)

### 기본 문제 목록
추가하기 전 기본 문제 5개입니다.
![기본 퀴즈 목록](docs/screenshots/list.png)

### 퀴즈 추가와 파일 저장
![퀴즈 추가와 저장 완료](docs/screenshots/add_quiz.png)

### 랜덤 출제와 정답·오답 판정
목록의 두 번째 문제인 리스트 문제가 마지막에 출제되는 등 원래 목록과 다른 순서로 출제됩니다.
![플레이 앞부분](docs/screenshots/play.png)
![플레이 중간 부분](docs/screenshots/play-middle.png)

### 최종 결과
6문제 중 2개 정답으로 33점을 기록했습니다.
![최종 결과 33점](docs/screenshots/result.png)

### 최고 점수 확인
![최고 점수 확인](docs/screenshots/score.png)

### 종료 후 재실행
추가한 문제를 포함한 6개 문제와 최고 점수 33점이 유지됩니다.
![재실행과 데이터 유지](docs/screenshots/restart.png)

### 개발 환경
Python 3.14.6, Git 2.55.0과 Git 사용자 설정을 확인했습니다.
![Python 버전과 Git 설정](docs/screenshots/environment.png)

### Git 커밋과 브랜치 병합 기록
캡처 시점의 커밋 15개와 `feature/quiz-play` 브랜치의 생성·병합을 확인할 수 있습니다. 이후 자료 추가 커밋은 이 이미지에 포함되지 않습니다.
![Git 커밋 그래프와 브랜치 병합](docs/screenshots/git-log.png)

캡처: 2026-11-04 21:29:17 KST, 당시 main에서 도달 가능한 커밋 15개. 상단 `f068698`의 커밋 시각은 2026-11-04 21:27:49 +09:00이며, 이후 추가한 커밋은 이미지에 없습니다. `feature/quiz-play`의 `a85ff88`은 출제·정답 판정·결과 표시 구현이고, `c38eac4`는 이를 main에 합친 병합 커밋입니다. 커밋 시각과 개수는 아래 명령으로 현재 이력에서 확인할 수 있습니다.

```sh
git log --format="%h %cI %s" --all
git rev-list --count HEAD
```

자동 테스트 로그와 실제 실행 캡처는 별도로 관리합니다. 이 README에는 실제로 존재하는 이미지 파일만 연결했습니다.

GitHub 복제 실습을 완료했습니다.


## GitHub 업로드와 clone/pull 실습 증거

### main 및 기능 브랜치 업로드 (2026-11-04)
![두 브랜치 GitHub 업로드 성공](docs/screenshots/push.png)

### 별도 폴더로 clone (2026-11-08)
![GitHub 저장소 복제 성공](docs/screenshots/clone.png)

### 복제본에서 README 수정, commit, push
복제 폴더에서 확인 문구를 추가하고 `b671389` 커밋을 만든 뒤 원격 main에 반영했습니다.
![복제본 README 변경과 업로드](docs/screenshots/clone-push.png)

### 원래 폴더에서 pull 및 반영 확인
`git pull --ff-only`로 `03f76b0`에서 `b671389`로 이동했습니다. `git log -1`과 `tail -3 README.md`로 같은 커밋 및 추가 문구를 확인했습니다.
![원래 폴더에서 pull과 변경 반영 확인](docs/screenshots/pull.png)
