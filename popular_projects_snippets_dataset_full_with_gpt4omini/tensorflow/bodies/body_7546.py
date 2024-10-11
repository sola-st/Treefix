# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn_expected_to_exit_with_20():
    if multi_worker_test_base.get_task_type() == 'worker':
        time.sleep(10000)
    sys.exit(20)

mpr = multi_process_runner.MultiProcessRunner(
    fn_expected_to_exit_with_20,
    multi_worker_test_base.create_cluster_spec(
        has_chief=True, num_workers=1))
mpr.start()

with self.assertRaisesRegex(
    multi_process_runner.UnexpectedSubprocessExitError,
    'Subprocess chief-0 exited with exit code 20'):
    mpr.join()
