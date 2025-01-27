# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    with self.assertRaisesOpError("Elements cannot be smaller than 0."):
        x = array_ops.placeholder(dtype=dtypes.int32)
        x_checked = du.embed_check_integer_casting_closed(
            x, target_dtype=dtypes.uint16, assert_nonnegative=False)
        x_checked.eval(feed_dict={x: np.array([1, -1], dtype=np.int32)})
