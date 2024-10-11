# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
shape = [4, 4]
indices = [0, 1, 2, 2]
for tf_op in [
    math_ops.segment_sum, math_ops.segment_mean, math_ops.segment_min,
    math_ops.segment_max
]:
    with self.cached_session():
        tf_x, np_x = self._input(shape, dtype=dtypes_lib.float64)
        s = tf_op(data=tf_x, segment_ids=indices)
        jacob_t, jacob_n = gradient_checker.compute_gradient(
            tf_x,
            shape,
            s, [3, 4],
            x_init_value=np_x.astype(np.double),
            delta=1)
    self.assertAllClose(jacob_t, jacob_n)
