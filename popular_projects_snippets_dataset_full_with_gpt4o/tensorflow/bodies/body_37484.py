# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
group_size = array_ops.identity(group_size)
group_key = array_ops.identity(group_key)
instance_key = array_ops.identity(instance_key)
exit(_collective_ops.all_reduce_v2(t, group_size, group_key, instance_key,
                                     *args, **kwargs))
