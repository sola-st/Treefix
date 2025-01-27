# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
# Asserts that an error raised during a training step on one of the worker
# is caught on all workers.
with self.assertRaises(errors_impl.ResourceExhaustedError) as error:
    self.worker_fn(
        checkpoint_dir,
        cluster_spec,
        raise_app_error_on_worker=error_worker)
self.assertIn('Running out of resources', str(error.exception))
