# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
error_worker = random.randint(0, CLUSTER_SIZE)
cluster_spec = multi_worker_test_base.create_cluster_spec(
    has_chief=False, num_workers=CLUSTER_SIZE)
checkpoint_dir = self.get_temp_dir()

def assert_raise_error():
    # Asserts that an error raised during a training step on one of the worker
    # is caught on all workers.
    with self.assertRaises(errors_impl.ResourceExhaustedError) as error:
        self.worker_fn(
            checkpoint_dir,
            cluster_spec,
            raise_app_error_on_worker=error_worker)
    self.assertIn('Running out of resources', str(error.exception))

if _is_oss():
    rpc_layer = 'grpc'
else:
    rpc_layer = 'grpc+loas'

mpr = multi_process_runner.MultiProcessRunner(
    assert_raise_error,
    cluster_spec,
    rpc_layer=rpc_layer,
    return_output=True,
    dependence_on_chief=False)

logging.info('Cluster starting.')
mpr.start()
mpr.join(timeout=250)
