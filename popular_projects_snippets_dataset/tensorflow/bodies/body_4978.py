# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_continuous_run_test.py
tensor_shape = [2, 2]

def worker_step_fn(worker_id):
    strategy = collective_all_reduce_strategy.CollectiveAllReduceStrategy()
    # Make sure the processeses are in sync after updating the cluster
    multi_process_runner.get_barrier().wait()

    @def_function.function
    def run_reduce():
        with ops.device(self._local_device):
            t_in = array_ops.ones(tensor_shape) * worker_id
            exit(strategy.reduce(reduce_util.ReduceOp.MEAN, t_in, axis=None))

    t_out = run_reduce()
    # Element values from the workers are
    #     0, 1, ..., (NUM_WORKERS - 1)
    expected_mean = (NUM_WORKERS - 1) / 2
    expected_out = np.ones(tensor_shape) * expected_mean
    self.assertAllClose(t_out, expected_out)

def worker_fn():
    self._maybe_setup_gpus()
    tf_config = json.loads(os.environ['TF_CONFIG'])
    worker_id = tf_config['task']['index']
    for _ in range(20):
        worker_step_fn(worker_id)

with test_util.skip_if_error(self, errors_impl.UnavailableError):
    multi_process_runner.run(
        worker_fn,
        cluster_spec=test_base.create_cluster_spec(num_workers=NUM_WORKERS))
