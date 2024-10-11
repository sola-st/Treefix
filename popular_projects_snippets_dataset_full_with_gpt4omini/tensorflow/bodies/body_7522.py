# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
runner = multi_process_runner.MultiProcessRunner(
    fn_that_errors,
    multi_worker_test_base.create_cluster_spec(num_workers=1, num_ps=1),
    max_run_time=20)
runner.start()
with self.assertRaisesRegex(ValueError, 'This is an error.'):
    runner.join()
