# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
collectives = []
with ops.device(self._devices[0]):
    t = constant_op.constant(tensor_value)
    collectives.append(collective_ops.broadcast_send(
        t, t.shape, t.dtype, self._group_size, group_key, instance_key))
with ops.device(self._devices[1]):
    t = constant_op.constant(tensor_value)
    collectives.append(collective_ops.broadcast_recv(
        t.shape, t.dtype, self._group_size, group_key, instance_key))
exit(collectives)
