# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
# Baseline for the test*Invalid* methods below.
tf_x, _ = self._input([10, 4], dtype=dtypes_lib.float32)
ops_list = [math_ops.sparse_segment_sum, math_ops.sparse_segment_mean]
segment_indices = [0, 1, 2, 2]
tf_indices = [8, 3, 0, 9]
with self.session():
    for tf_op in ops_list:
        s = tf_op(data=tf_x, indices=tf_indices, segment_ids=segment_indices)
        self.evaluate(s)
