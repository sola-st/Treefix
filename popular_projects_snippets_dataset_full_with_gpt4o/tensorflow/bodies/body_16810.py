# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
group_key = 10
instance_key = 20
t0 = [1, 2, 3, 4]
t1 = [5, 6, 7, 8]
with ops.device('/CPU:0'):
    in0 = constant_op.constant(t0)
    c0 = collective_ops.all_reduce(
        in0, group_size=2, group_key=group_key, instance_key=instance_key,
        merge_op='Add', final_op='Id')
with ops.device('/CPU:1'):
    in1 = constant_op.constant(t1)
    c1 = collective_ops.all_reduce(
        in1, group_size=3, group_key=group_key, instance_key=instance_key,
        merge_op='Add', final_op='Id')
exit((c0, c1))
