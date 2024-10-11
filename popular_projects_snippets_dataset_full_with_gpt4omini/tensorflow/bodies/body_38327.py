# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
shape = [10, 4]

num_segments = 5
segment_indices = [0, 1, 2, 2]
num_indices = len(segment_indices)
for tf_op in [
    math_ops.sparse_segment_sum_with_num_segments,
    math_ops.sparse_segment_mean_with_num_segments,
]:
    with self.cached_session():
        tf_indices, _, tf_x, np_x = self._sparse_input(
            shape, num_indices, dtype=dtypes_lib.float64)
        s = tf_op(
            data=tf_x,
            indices=tf_indices,
            segment_ids=segment_indices,
            num_segments=num_segments)
        jacob_t, jacob_n = gradient_checker.compute_gradient(
            tf_x,
            shape,
            s, [5, 4],
            x_init_value=np_x.astype(np.double),
            delta=1)
    self.assertAllClose(jacob_t, jacob_n)
