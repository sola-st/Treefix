# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py

def fn():
    logging.info('Running')
    time.sleep(1)
    raise ValueError

mpr = multi_process_runner.MultiProcessRunner(
    fn,
    multi_worker_test_base.create_cluster_spec(num_workers=1),
    auto_restart=True,
    return_output=True)
mpr.start()
with self.assertRaises(ValueError) as cm:
    mpr.join(timeout=10)
self.assertGreater(
    sum(['Running' in msg for msg in cm.exception.mpr_result.stdout]), 1)
