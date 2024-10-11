# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
self._setup_context()

tensor_value = [0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1]
group_key = 1
instance_key = 1

@def_function.function
def run_nccl_broadcast_double_send():
    for device in self._devices:
        with ops.device(device):
            t = constant_op.constant(tensor_value)
            collective_ops.broadcast_send(
                t, t.shape, t.dtype, self._group_size, group_key, instance_key)

with self.assertRaisesRegex(errors.InternalError, 'already has source'):
    run_nccl_broadcast_double_send()
