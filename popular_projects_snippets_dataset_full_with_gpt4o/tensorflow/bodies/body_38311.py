# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
tf_x = constant_op.constant([], shape=[0, 4], dtype=dtypes_lib.float32)
ops_list = [
    math_ops.sparse_segment_sum_with_num_segments,
    math_ops.sparse_segment_mean_with_num_segments
]
segment_indices = []
tf_indices = []
num_segments = 5
with self.session():
    for tf_op in ops_list:
        s = tf_op(
            data=tf_x,
            indices=tf_indices,
            segment_ids=segment_indices,
            num_segments=num_segments)
        tf_ans = self.evaluate(s)
        self.assertAllClose(np.zeros([5, 4]), tf_ans)
