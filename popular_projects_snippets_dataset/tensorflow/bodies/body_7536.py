# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
mpr = multi_process_runner.MultiProcessRunner(
    fn_that_errors,
    multi_worker_test_base.create_cluster_spec(num_workers=2),
    return_output=True)
mpr.start()
time.sleep(60)
mpr.terminate_all()
with self.assertRaisesRegex(ValueError, 'This is an error.'):
    mpr.join()
