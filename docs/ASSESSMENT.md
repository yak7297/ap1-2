# 평가 항목별 구현·문서 근거

두 번째 평가의 20개 항목에 대해 실제 파일과 README 본문의 위치를 정리했습니다. 아래는 자체 점검 자료이며 외부 평가 통과 결과를 뜻하지 않습니다.

| 항목 | 구현·문서 근거 |
| --- | --- |
| 1 메뉴 | game.py의 show_menu()/run(), 메뉴 흐름 주석, docs/USAGE.md 주요 출력 |
| 2 정오답·입력 | Quiz.is_correct(), inputs.read_text()/read_number(), USAGE의 입력 사례 표 |
| 3 파일 유지 | state.json의 문제 6개·최고 33점, restart.png, 저장/로드 테스트와 README 저장 정책 |
| 4 기본 문제 | defaults.default_quizzes()의 직접 작성 5개, README의 향후 difficulty/source 확장 설계 |
| 5 커밋·업로드 | README의 원격 URL·커밋 수·최근 이력 스냅샷, 실제 Git 이력 |
| 6 브랜치·병합 | a85ff88 기능 구현, c38eac4 병합, git-log.png, README 및 SUBMISSION의 설명 |
| 7 clone/push/pull | clone.png, clone-push.png, pull.png, screenshots/README의 명령·캡처 시각 |
| 8 클래스 책임 | [README 본문: 책임과 경계 표](../README.md#class-responsibilities) |
| 9 입력/IO 분리 근거 | [README 본문: 재사용·오류 경계·독립 테스트 이유](../README.md#input-io-design) |
| 10 저장 경로·로드 순서 | storage.STATE_PATH/StateStore.load(), USAGE의 읽기→검증→복구 설명 |
| 11 Ctrl+C/EOF | main.main()의 except/finally, README의 중단 상태별 저장 정책 표 |
| 12 커밋 규칙 | README의 프리픽스·권장 변경 단위·실제 메시지 4개, LEARNING의 전체 예시 |
| 13 클래스 선택 이유 | [README 본문: 객체지향 선택 이유 및 절차적 구현 장단점](../README.md#object-oriented-reasons) |
| 14 JSON 선택 | README의 가독성·표준 라이브러리 이유, SQLite/DB/append 로그 장단점 |
| 15 파일 예외 | StateStore.load()/save()의 예외 처리, README의 성공/실패·재시도·로그 정책 |
| 16 브랜치 전략 | main/feature 구분, --no-ff 병합, PR·보호 설정 실제 적용 범위 설명 |
| 17 데이터 설계 | README 필드 설명 및 호환성·버전·이관 방침. 미래 기능과 현재 구현 구분 |
| 18 JSON 한계 | README의 시간·메모리·동시성 한계와 100/1000/10000문제 실제 측정, 원문 JSON |
| 19 백업·복구 | StateStore.load()의 백업·기본값 복구, README의 개수 제한 없음·수동 정리 정책 |
| 20 변경 영향도 | [README 본문: 요구변경별 파일·메서드·영향·검증 표](../README.md#change-impact) |

핵심 설계 #8/#9/#13/#20은 다른 문서 링크를 열지 않아도 루트 README의 설계 설명 절에 포함되어 있습니다. 실제 성능 측정은 Python 3.14.6에서 임시 폴더로 실행했으며 최적화나 데이터베이스를 새로 구현한 것은 아닙니다. 코드의 기능 변경은 없고 메뉴 설명 주석만 추가했습니다.
