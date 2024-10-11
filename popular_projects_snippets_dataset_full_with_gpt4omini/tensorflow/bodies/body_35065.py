# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session() as sess:
    x = array_ops.placeholder(dtypes.float32)
    shift = array_ops.placeholder(dtypes.int32)
    for x_value in (np.ones(
        1, dtype=x.dtype.as_numpy_dtype()), np.ones(
            (2, 1), dtype=x.dtype.as_numpy_dtype()), np.ones(
                (3, 2, 1), dtype=x.dtype.as_numpy_dtype())):
        for shift_value in np.arange(-5, 5):
            self.assertAllEqual(
                self._np_rotate_transpose(x_value, shift_value),
                sess.run(du.rotate_transpose(x, shift),
                         feed_dict={x: x_value,
                                    shift: shift_value}))
