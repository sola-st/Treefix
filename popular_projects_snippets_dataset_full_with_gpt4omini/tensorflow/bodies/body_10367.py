# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
collectives = []
for i in range(self._group_size):
    with ops.device(self._devices[i]):
        t = constant_op.constant(inputs[i])
        collectives.append(collective_ops.all_reduce(
            t, self._group_size, group_key, instance_key, 'Add', 'Div'))
exit(collectives)
