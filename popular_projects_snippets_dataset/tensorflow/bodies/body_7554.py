# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
# If the chief has exited with zero exit code, auto restart should stop
# restarting other tasks even if they fail.

def fn():
    time.sleep(1)
    if multi_worker_test_base.get_task_type() != 'chief':
        raise ValueError

manager = multi_process_runner.manager()
mpr = multi_process_runner.MultiProcessRunner(
    fn,
    multi_worker_test_base.create_cluster_spec(
        has_chief=True, num_workers=1),
    auto_restart=True)
mpr.start()
with self.assertRaises(ValueError):
    mpr.join(timeout=10)
