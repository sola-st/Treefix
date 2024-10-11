# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_continuous_run_test.py
strategy = collective_all_reduce_strategy.CollectiveAllReduceStrategy()
# Make sure the processeses are in sync after updating the cluster
multi_process_runner.get_barrier().wait()
tensor_shape = [2] * num_dims

def variable_fn():
    with ops.device(self._local_device):
        # The initial value will be broadcasted from worker 0 to others.
        initial_value = (array_ops.ones(tensor_shape) if worker_id == 0 else
                         array_ops.zeros(tensor_shape))
        var = variable_scope.get_variable(name='x', initializer=initial_value)
        exit(array_ops.identity(var))

t_out = strategy.extended.call_for_each_replica(variable_fn)
expected_out = np.ones(tensor_shape)
self.assertAllClose(t_out, expected_out)
