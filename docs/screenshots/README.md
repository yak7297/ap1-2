# 실제 캡처 목록과 시각

사용자가 제공한 PNG를 수정하지 않고 복사했습니다. 아래 캡처 시각은 사용자가 첨부한 원본 파일명에 기록된 한국 시각(KST)이며 Git 커밋 시각과는 별개입니다. 총 14개입니다.

| 파일 | 캡처 시각 (KST) | 확인 내용 | 실행 명령·입력 |
| --- | --- | --- | --- |
| [menu.png](menu.png) | 2026-11-04 21:13:02 | VS Code 메뉴 실행 | `python3 main.py` |
| [list.png](list.png) | 2026-11-04 21:18:17 | 기본 문제 5개 목록 | `메뉴 3` |
| [add_quiz.png](add_quiz.png) | 2026-11-04 21:20:23 | 문제 추가와 저장 | `메뉴 2 및 문제/선택지/정답 입력` |
| [play.png](play.png) | 2026-11-04 21:22:17 | 플레이 앞부분 | `메뉴 1 및 정답 입력` |
| [play-middle.png](play-middle.png) | 2026-11-04 21:22:22 | 플레이 중간 | `정답 입력 (같은 게임)` |
| [result.png](result.png) | 2026-11-04 21:22:26 | 6문제 중 2개 정답, 33점 | `6번째 답 입력 후 결과` |
| [score.png](score.png) | 2026-11-04 21:23:06 | 최고 점수 | `메뉴 4` |
| [restart.png](restart.png) | 2026-11-04 21:23:32 | 재실행 후 6개·33점 유지 | `메뉴 5 → python3 main.py → 메뉴 4` |
| [environment.png](environment.png) | 2026-11-04 21:27:21 | Python·Git 버전과 사용자 설정 | `python3 --version / git --version / git config user.name / git config user.email` |
| [git-log.png](git-log.png) | 2026-11-04 21:29:17 | 캡처 당시 커밋 15개·브랜치 병합 | `git --no-pager log --oneline --graph --all` |
| [push.png](push.png) | 2026-11-04 21:31:53 | main·기능 브랜치 업로드 | `git push -u origin main / git push origin feature/quiz-play` |
| [clone.png](clone.png) | 2026-11-08 12:07:05 | 원격 저장소 복제 | `git clone … python-quiz-game-clone / cd python-quiz-game-clone` |
| [clone-push.png](clone-push.png) | 2026-11-08 12:09:40 | 복제본 변경·commit·push | `printf … >> README.md / git add / git commit / git push` |
| [pull.png](pull.png) | 2026-11-08 12:10:51 | 원래 폴더에서 pull·문구 확인 | `cd ../python-quiz-game / git pull --ff-only / git log -1 / tail -3 README.md` |

기본 목록 사진은 문제를 추가하기 전 5개 상태입니다. 추가 후 6개와 최고 점수 유지는 restart.png에서 확인합니다. git-log.png에는 캡처 당시 15개 커밋만 표시되며 이후 커밋은 현재 Git 이력을 확인해야 합니다. 이미지 자체에 글자나 시각을 덧씌우지 않았습니다.
