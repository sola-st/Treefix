# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
cluster_spec = multi_worker_test_base.create_cluster_spec(num_workers=2)
runner = multi_process_runner.MultiProcessPoolRunner(cluster_spec)
pid = runner.run(fn_that_returns_pid)
with self.assertRaisesRegex(ValueError, 'This is an error.'):
    runner.run(fn_that_errors)
self.assertAllEqual(runner.run(fn_that_returns_pid), pid)
