# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
self._setup_context()

tensor_value = [0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1]
group_key = 1
instance_key = 1

@def_function.function
def run_basic_nccl_broadcast():
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

for result in run_basic_nccl_broadcast():
    self.assertAllClose(result, tensor_value, rtol=1e-5, atol=1e-5)
