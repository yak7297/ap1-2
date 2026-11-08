# 제출 점검표와 Git 실습 기록

## 현재 완료한 항목

- [x] 퀴즈 풀기/추가/목록/최고 점수/종료
- [x] Python 기초 주제 5문제와 4지선다
- [x] Quiz, QuizGame 클래스 및 기능별 메서드
- [x] 프로젝트 루트 state.json에 UTF-8 저장/불러오기
- [x] 입력 오류, Ctrl+C, EOF, 파일 손상 및 입출력 오류 안내
- [x] 보너스 1개: 랜덤 출제
- [x] 의미 있는 기능별 커밋 10개 이상
- [x] feature/quiz-play 브랜치 생성 및 main 병합
- [x] README 필수 항목과 자동 검증 결과
- [x] GitHub 저장소 생성: https://github.com/yak7297/ap1-2
- [x] 코드와 기존 자료를 GitHub로 push
- [ ] 이번에 추가한 Git 실습 증거와 문서 정리를 최종 push
- [x] GitHub 저장소 clone → README 변경 → commit → push → 원래 폴더 pull (2026-11-08, b671389)
- [x] 실제 실행 화면 캡처 8개를 README와 연결
- [x] Python 버전과 Git 설정 개발 환경 캡처
- [x] Git 그래프 실제 스크린샷
- [ ] GitHub URL 제출

## 실제 GitHub 업로드 기록 (완료)

GitHub 저장소 `yak7297/ap1-2`에 main과 feature/quiz-play 브랜치를 업로드했습니다. 아래는 이미 수행한 절차의 기록이며, remote add를 다시 실행할 필요는 없습니다.

VS Code 터미널이 이 프로젝트 폴더에 있는지 확인한 뒤, 아래의 실제 저장소 주소를 사용합니다.

```sh
git remote add origin https://github.com/yak7297/ap1-2.git
git push -u origin main
git push origin feature/quiz-play
```

GitHub 인증이 요청되면 본인의 인증 방식으로 로그인합니다. 비밀번호나 토큰을 소스 파일에 넣지 않습니다. 저장소 페이지에서 코드와 커밋이 보이는지 확인합니다.

초기 설정 직후 첫 push를 하는 수업 순서는 이미 로컬 구현이 진행되어 지금 소급해 수행할 수 없습니다. 지금 push하면 실제 로컬 개발 기록은 올라가지만 단계별 과거 push까지 증명되지는 않습니다. 수업에서 초기 push 시점까지 별도 평가한다면 담당자에게 확인하세요.

## clone과 pull 실습 (완료, 재현 절차)

기존 프로젝트 폴더 바로 옆에 복제본을 생성합니다. 같은 이름의 복제 폴더가 이미 있으면 새 이름을 사용합니다.

```sh
cd ..
git clone https://github.com/yak7297/ap1-2.git python-quiz-game-clone
cd python-quiz-game-clone
```

복제 폴더의 README 맨 아래에 `GitHub 복제 실습을 완료했습니다.` 한 줄을 직접 추가한 뒤 실행합니다.

```sh
git add README.md
git commit -m "Docs: 복제 저장소에서 Git 실습 확인 문구 추가"
git push
cd ../python-quiz-game
git pull --ff-only
git log -1 --oneline
```

원래 폴더 README에도 추가한 한 줄이 나타나야 성공입니다. 터미널의 clone/push/pull 결과를 실제 화면으로 캡처하거나 원문 로그로 보관합니다. 아직 수행하지 않은 과정을 수행 완료로 표시하지 않습니다.

## 스크린샷

macOS에서 Shift+Command+4를 눌러 실제 터미널 또는 VS Code 화면을 캡처합니다. 권장 파일 이름:

| 파일 | 화면에 보여야 할 내용 |
| --- | --- |
| docs/screenshots/environment.png | VS Code, `python3 --version`, `git --version`, `git config user.name`, `git config user.email` |
| docs/screenshots/menu.png | `python3 main.py` 실행 후 메뉴 |
| docs/screenshots/add_quiz.png | 문제/선택지/정답 입력과 저장 완료 |
| docs/screenshots/list.png | 추가 전 기본 문제 5개 목록 (추가 후 6개 상태는 restart.png에서 확인) |
| docs/screenshots/play.png, result.png | 플레이 중 정답/오답과 최종 결과 (확보 완료) |
| docs/screenshots/score.png | 최고 점수 확인 |
| docs/screenshots/restart.png | 종료 후 재실행하여 추가 문제와 최고 점수 유지 확인 |
| docs/screenshots/git-log.png | `git log --oneline --graph --all` 결과 |
| docs/screenshots/push.png, clone.png, clone-push.png, pull.png | 원격 업로드 및 clone/변경/push/pull 성공 결과 |

캡처한 이미지를 저장한 뒤 최종 업로드합니다.

```sh
git add docs/screenshots
git commit -m "Docs: 프로그램 실행과 Git 실습 화면 추가"
git push
```

## 마지막 확인

GitHub에서 README, 코드, state.json, 스크린샷과 10개 이상의 커밋이 보이는지 확인합니다. GitHub 저장소 URL과 수업에서 요구한 이미지 파일을 제출합니다. 자동 테스트 성공만으로 원격 업로드와 캡처 제출이 완료된 것은 아닙니다.

실제 캡처 14개는 docs/screenshots/README.md에 정리했습니다. 2026-11-04 업로드와 2026-11-08 clone/push/pull 실습에 성공했습니다. Git 실습 마지막 커밋 b671389과 README 문구 반영을 캡처 및 로컬 이력으로 확인했습니다. 이번 증거 정리 변경은 최종 push가 필요합니다.
