# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn():
    time.sleep(100000)

mpr = multi_process_runner.MultiProcessRunner(
    fn, multi_worker_test_base.create_cluster_spec(num_workers=1))
mpr.start()
self.assertTrue(mpr.process_exists('worker', 0))
mpr.terminate('worker', 0)
# Worker 0 should exit at some point, or else the test would time out.
while mpr.process_exists('worker', 0):
    time.sleep(1)
