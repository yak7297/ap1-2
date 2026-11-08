"""임시 폴더에서 JSON 저장/불러오기 규모를 측정합니다."""
import contextlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import platform
import statistics
import sys
import tempfile
import time
import tracemalloc

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from defaults import default_quizzes
from quiz import Quiz
from storage import StateStore


def measure():
    results = []
    with tempfile.TemporaryDirectory() as folder:
        store = StateStore(Path(folder) / 'state.json')
        template = default_quizzes()[0]
        for count in (100, 1000, 10000):
            state = store.default_state()
            state['quizzes'] = [Quiz(f'측정용 문제 {i}: {template.question}', template.choices, template.answer)
                                for i in range(count)]
            saves, loads = [], []
            for _ in range(3):
                start = time.perf_counter()
                if not store.save(state):
                    raise RuntimeError('측정용 저장 실패')
                saves.append((time.perf_counter() - start) * 1000)
                start = time.perf_counter()
                with contextlib.redirect_stdout(io.StringIO()):
                    loaded = store.load()
                loads.append((time.perf_counter() - start) * 1000)
                assert len(loaded['quizzes']) == count
            # 메모리 추적 오버헤드가 위 시간 측정에 섞이지 않도록 별도 실행합니다.
            tracemalloc.start()
            with contextlib.redirect_stdout(io.StringIO()):
                loaded = store.load()
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            results.append({'quizzes': count, 'file_bytes': store.path.stat().st_size,
                            'save_median_ms': round(statistics.median(saves), 3),
                            'load_median_ms': round(statistics.median(loads), 3),
                            'load_python_peak_bytes': peak})
    return {'measured_at_utc': datetime.now(timezone.utc).isoformat(),
            'python': platform.python_version(), 'platform': platform.platform(),
            'samples_per_size': 3,
            'method': 'Temporary directory; full StateStore.save/load; timing median without tracing; separate load peak via tracemalloc, excludes pre-existing objects and native/process memory.',
            'results': results}


if __name__ == '__main__':
    print(json.dumps(measure(), ensure_ascii=False, indent=2))
