# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
tf_x, _ = self._input([2, 4], dtype=dtypes_lib.float32)
ops_list = [
    math_ops.sparse_segment_sum_grad, math_ops.sparse_segment_mean_grad,
    math_ops.sparse_segment_sqrt_n_grad
]
segment_indices = [-1, 0, 1, 1]
tf_indices = [8, 3, 0, 9]
with self.session(use_gpu=False):
    for tf_op in ops_list:
        s = tf_op(tf_x, tf_indices, segment_indices, 10)
        with self.assertRaisesOpError(r"Segment id -1 out of range \[0, 2\)"):
            self.evaluate(s)
