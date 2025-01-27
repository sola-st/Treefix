# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

if multi_process_runner.is_oss():
    self.skipTest('Intentionally skipping longer test in OSS.')

def fn():
    time.sleep(250)
    raise ValueError('Worker 0 errored')

mpr = multi_process_runner.MultiProcessRunner(
    fn, multi_worker_test_base.create_cluster_spec(num_workers=1))

mpr.start()
with self.assertRaisesRegex(ValueError, 'Worker 0 errored'):
    mpr.join(timeout=None)
