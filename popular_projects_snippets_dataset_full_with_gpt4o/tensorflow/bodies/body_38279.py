# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
shape = [4, 4]
tf_x, _ = self._input(shape)
indices = constant_op.constant([0, 1, 2, 2], shape=[2, 2])
with self.assertRaises(ValueError):
    math_ops.segment_sum(data=tf_x, segment_ids=indices)
