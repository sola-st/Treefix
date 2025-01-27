# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn():
    logging.info('something printed')
    time.sleep(10000)  # Intentionally make the test timeout.

with self.assertRaises(multi_process_runner.SubprocessTimeoutError) as cm:
    mpr = multi_process_runner.MultiProcessRunner(
        fn,
        multi_worker_test_base.create_cluster_spec(num_workers=1),
        return_output=True)
    mpr.start()
    mpr.join(timeout=60)
mpr.terminate_all()

list_to_assert = cm.exception.mpr_result.stdout
self.assertTrue(
    any('something printed' in line for line in list_to_assert))
