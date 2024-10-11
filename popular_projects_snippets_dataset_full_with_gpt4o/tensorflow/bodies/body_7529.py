# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
for i in range(0, 10):
    print(
        'index {}, iteration {}'.format(self._worker_idx(), i), flush=True)
    time.sleep(1)
