# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
self._create_model_and_run_indefinitely()
self._cluster.kill_task("ps", 0)
while self.cluster_coord._cluster.closure_queue._error is None:
    time.sleep(1)
with self.assertRaises((errors.UnavailableError, errors.NotFoundError,
                        errors.FailedPreconditionError)):
    self.cluster_coord.join()
