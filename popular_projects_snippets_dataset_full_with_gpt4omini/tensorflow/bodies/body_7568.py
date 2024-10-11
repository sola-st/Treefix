# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
# When there's an exception in the main process, __del__() is not called.
# This test is to verify MultiProcessPoolRunner can cope with __del__() not
# being called.
cluster_spec = multi_worker_test_base.create_cluster_spec(
    has_chief=True, num_workers=2)
runner = multi_process_runner.MultiProcessPoolRunner(cluster_spec)
runner.run(fn_that_returns_pid)
raise ValueError('failure')
