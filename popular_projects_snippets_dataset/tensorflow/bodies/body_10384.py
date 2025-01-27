# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
self._setup_context()

group_key = 10
instance_key = 20
t0 = [1, 2, 3, 4]
t1 = [5, 6, 7, 8]

@def_function.function
def run_collective_device_mismatch():
    with ops.device('/CPU:0'):
        in0 = constant_op.constant(t0)
        collective_ops.all_reduce(in0, self._group_size, group_key,
                                  instance_key, 'Add', 'Id')
    with ops.device('/GPU:0'):
        in1 = constant_op.constant(t1)
        collective_ops.all_reduce(in1, self._group_size, group_key,
                                  instance_key, 'Add', 'Id')

with self.assertRaisesRegex(errors.InternalError,
                            'but that group has type'):
    run_collective_device_mismatch()
