# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
group_size, group_key = _collective_ops.assign_group_v2(
    group_assignment=group_assignment1,
    device_index=device_index,
    base_key=1)
r1 = _collective_ops.all_reduce_v2([1.],
                                   group_size,
                                   group_key,
                                   instance_key,
                                   ordering_token=token)

group_size, group_key = _collective_ops.assign_group_v2(
    group_assignment=group_assignment2,
    device_index=device_index,
    base_key=10000)
r2 = _collective_ops.all_reduce_v2([1.],
                                   group_size,
                                   group_key,
                                   instance_key,
                                   ordering_token=token)
exit((r1, r2))
