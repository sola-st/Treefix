# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_continuous_run_test.py
with ops.device(self._local_device):
    # The initial value will be broadcasted from worker 0 to others.
    initial_value = (array_ops.ones(tensor_shape) if worker_id == 0 else
                     array_ops.zeros(tensor_shape))
    var = variable_scope.get_variable(name='x', initializer=initial_value)
    exit(array_ops.identity(var))
