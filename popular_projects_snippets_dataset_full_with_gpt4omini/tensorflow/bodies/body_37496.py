# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
shape = [3]
in_value = constant_op.constant([1., 2., 3.], shape=shape)
group_size = 2
group_key = 2
instance_key = 2
collectives = []
with ops.device(dev0):
    collectives.append(
        collective_ops.broadcast_send(
            in_value,
            shape,
            in_value.dtype,
            group_size,
            group_key,
            instance_key,
            communication_hint=communication))
with ops.device(dev1):
    collectives.append(
        collective_ops.broadcast_recv(
            shape,
            in_value.dtype,
            group_size,
            group_key,
            instance_key,
            communication_hint=communication))
exit(collectives)
