# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
self._setup_context()

inputs = [[0, 1], [2, 3]]
group_key = 1
instance_key = 50

@def_function.function
def run_int32_error():
    for i in range(self._group_size):
        with ops.device(self._devices[i]):
            t = constant_op.constant(inputs[i], dtype=dtypes.int32)
            collective_ops.all_reduce(
                t, self._group_size, group_key, instance_key, 'Add', 'Div')

with self.assertRaisesRegex(
    errors.InternalError,
    'does not support datatype DT_INT32 on DEVICE_GPU'):
    run_int32_error()
