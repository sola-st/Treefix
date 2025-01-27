# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_continuous_run_test.py
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
