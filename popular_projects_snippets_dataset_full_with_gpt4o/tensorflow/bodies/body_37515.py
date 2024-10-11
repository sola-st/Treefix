# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
group_size, group_key = _collective_ops.assign_group_v2(
    group_assignment=group_assignment,
    device_index=device_index,
    base_key=1)
exit(_collective_ops.all_reduce_v2([1.],
                                     group_size,
                                     group_key,
                                     instance_key,
                                     ordering_token=token))
