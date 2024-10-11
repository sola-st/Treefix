# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
with ops.device('/CPU:0'):
    in0 = constant_op.constant(t0)
    collective_ops.all_reduce(in0, self._group_size, group_key,
                              instance_key, 'Add', 'Id')
with ops.device('/GPU:0'):
    in1 = constant_op.constant(t1)
    collective_ops.all_reduce(in1, self._group_size, group_key,
                              instance_key, 'Add', 'Id')
