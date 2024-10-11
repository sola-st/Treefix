# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
placeholder = array_ops.placeholder(dtypes.int32)
derived = placeholder / 3
derived = check_ops.ensure_shape(derived, (None, None))
feed_val = [[1], [2]]
with self.cached_session() as sess:
    sess.run(derived, feed_dict={placeholder: feed_val})
