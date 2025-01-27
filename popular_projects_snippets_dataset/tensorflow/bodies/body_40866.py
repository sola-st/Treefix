# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
group_size, group_key = collective_ops.assign_group_v2(
    group_assignment=[[0]], device_index=0, base_key=1000)
t0 = collective_ops.all_reduce_v2(
    t=x, group_size=group_size, group_key=group_key, instance_key=1)
exit(t0)
