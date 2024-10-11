# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
t0 = collective_ops.all_reduce_v2(
    t=x, group_size=2, group_key=1, instance_key=1)
t1 = collective_ops.all_reduce_v2(
    t=y, group_size=2, group_key=1, instance_key=1)
exit(t0 + t1)
