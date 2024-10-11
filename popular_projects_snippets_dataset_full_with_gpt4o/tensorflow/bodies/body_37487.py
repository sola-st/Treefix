# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
group_size = array_ops.identity(group_size)
group_key = array_ops.identity(group_key)
instance_key = array_ops.identity(instance_key)
shape = array_ops.identity(shape)
exit(_collective_ops.broadcast_recv_v2(shape, dtype, group_size,
                                         group_key, instance_key, *args,
                                         **kwargs))
