# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
# Test the case when worker-0 fails immediately after worker-1 restarts.

def fn():
    time.sleep(5)

mpr = multi_process_runner.MultiProcessRunner(
    fn,
    multi_worker_test_base.create_cluster_spec(
        has_chief=False, num_workers=2),
    auto_restart=True)
mpr.start()
pid = mpr.get_process_id('worker', 1)
mpr.terminate('worker', 1)
while mpr.get_process_id('worker', 1) == pid:
    time.sleep(0.1)
mpr.terminate('worker', 0)
mpr.join(timeout=20)
