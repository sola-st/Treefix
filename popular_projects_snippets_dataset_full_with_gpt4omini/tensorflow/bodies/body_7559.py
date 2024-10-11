# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
if self._worker_idx() == 1:
    time.sleep(10000)
raise ValueError('Worker 0 errored')
