# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn():
    if self._worker_idx() == 1:
        time.sleep(10000)
    raise ValueError('Worker 0 errored')

mpr = multi_process_runner.MultiProcessRunner(
    fn, multi_worker_test_base.create_cluster_spec(num_workers=2))
mpr.start()

with self.assertRaisesRegex(
    ValueError,
    'Worker 0 errored'):
    mpr.join(timeout=20)
