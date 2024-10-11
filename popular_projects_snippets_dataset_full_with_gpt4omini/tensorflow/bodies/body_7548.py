# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn_expected_to_exit_with_10():
    sys.exit(10)

mpr = multi_process_runner.MultiProcessRunner(
    fn_expected_to_exit_with_10,
    multi_worker_test_base.create_cluster_spec(num_workers=1))
mpr.start()

with self.assertRaisesRegex(
    multi_process_runner.UnexpectedSubprocessExitError,
    'Subprocess worker-0 exited with exit code 10'):
    mpr.join()
