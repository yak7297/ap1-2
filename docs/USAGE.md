# 메뉴와 기능별 주요 출력 예시

아래는 [실제 실행 원문](evidence/console-session.txt)과 [재실행 원문](evidence/restart-session.txt)의 주요 출력을 발췌한 것입니다. 입력 파일은 [console-input.txt](evidence/console-input.txt)에 있습니다. 전체 로그와 별도로 읽기 쉽게 기능별로 모았으며, 프롬프트의 연속 반복은 생략했습니다. 랜덤 출제로 문제 순서는 실행마다 달라질 수 있습니다.

| 메뉴 | 주요 출력 | 실제 화면 |
| --- | --- | --- |
| 시작 | Python 기초 퀴즈 게임 / 1. 퀴즈 풀기 … 5. 종료 | [메뉴](screenshots/menu.png) |
| 1. 풀기 | 퀴즈를 시작합니다! 총 6문제 | [플레이](screenshots/play.png) |
| 정답 | 정답입니다! | [정답·오답](screenshots/play.png) |
| 오답 | 오답입니다. 정답: 2. int | [실행 원문](evidence/console-session.txt) |
| 결과 | 결과: 6문제 중 2문제 정답! (33점) / 새로운 최고 점수입니다! | [결과](screenshots/result.png) |
| 2. 추가 | 새로운 퀴즈를 추가합니다. / 퀴즈가 추가되었습니다. / 파일에 저장했습니다. | [추가](screenshots/add_quiz.png) |
| 3. 목록 | 등록된 퀴즈 목록 (총 5개), 추가 후 (총 6개) | [기본 목록](screenshots/list.png), [추가 후 원문](evidence/console-session.txt) |
| 4. 점수 | 최고 점수: 33점 (6문제 중 2문제 정답) | [점수](screenshots/score.png) |
| 5. 종료 | 게임을 종료합니다. / 데이터를 저장했습니다. 다음에 또 만나요! | [종료·재실행](screenshots/restart.png) |
| 재실행 | 저장된 데이터를 불러왔습니다. (퀴즈 6개, 최고점수 33점) | [재실행](screenshots/restart.png) |

오답은 정답 번호와 선택지 내용을 표시하고 정답 수를 늘리지 않습니다. 별도의 감점 없이 `round(정답 수 / 전체 문제 수 * 100)`으로 최종 점수를 계산합니다.

## 입력과 예외 안내

실행 원문에는 `숫자를 입력하세요.`, `1~5 사이의 숫자를 입력하세요.`, `빈 입력은 사용할 수 없습니다. 다시 입력하세요.`, `아직 퀴즈를 풀지 않았습니다.` 안내가 포함되어 있습니다.

Ctrl+C/EOF 시 안전 종료, 빈 목록, 파일 손상과 읽기/쓰기 실패는 [자동 테스트](evidence/tests.txt)에서 별도로 검증합니다. 해당 테스트 결과와 실제 사용자 캡처를 혼동하지 않습니다. 저장 시점과 복구 파일 위치는 [README](../README.md)의 데이터 설명을 참고하세요.
