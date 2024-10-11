# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
tf_x, _ = self._input([10, 4], dtype=dtypes_lib.float32)
ops_list = [
    math_ops.sparse_segment_sum_with_num_segments,
    math_ops.sparse_segment_mean_with_num_segments,
]
num_segments = -2
segment_indices = [0, 1, 3, 3]
tf_indices = [8, 3, 0, 9]
with self.session(use_gpu=False):
    for tf_op in ops_list:
        with self.assertRaisesRegex(
            ValueError, "Cannot specify a negative value for num_segments"):
            tf_op(
                data=tf_x,
                indices=tf_indices,
                segment_ids=segment_indices,
                num_segments=num_segments)
