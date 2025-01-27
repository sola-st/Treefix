# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
for device in self._devices:
    with ops.device(device):
        t = constant_op.constant(tensor_value)
        collective_ops.broadcast_recv(
            t.shape, t.dtype, self._group_size, group_key, instance_key)
