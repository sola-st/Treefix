# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.cached_session():
    with self.assertRaisesOpError("Elements must be int16-equivalent."):
        x = array_ops.placeholder(dtype=dtypes.float16)
        x_checked = du.embed_check_integer_casting_closed(
            x, target_dtype=dtypes.int16)
        x_checked.eval(feed_dict={x: np.array([1, 1.5], dtype=np.float16)})
