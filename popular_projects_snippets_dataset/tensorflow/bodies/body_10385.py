# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
t0 = [1., 20., 3., 40., 5.]
t1 = [10., 2., 30., 4., 50.]
with ops.device('/GPU:0'):
    in0 = constant_op.constant(t0)
    c0 = collective_ops.all_reduce(
        in0, self._group_size, group_key, instance_key, merge_op,
        final_op='Id', communication_hint='nccl')
with ops.device('/GPU:1'):
    in1 = constant_op.constant(t1)
    c1 = collective_ops.all_reduce(
        in1, self._group_size, group_key, instance_key, merge_op,
        final_op='Id', communication_hint='nccl')
exit((c0, c1))
