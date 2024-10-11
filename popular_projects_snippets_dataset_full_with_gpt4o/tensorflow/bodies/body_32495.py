# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
placeholder = array_ops.placeholder(dtypes.float32)
derived = check_ops.ensure_shape(placeholder, (None, None))
gradient = gradients.gradients(derived, placeholder)

feed_val = [[4.0], [-1.0]]
with self.cached_session() as sess:
    gradient_values, = sess.run(gradient, feed_dict={placeholder: feed_val})

expected = [[1.0], [1.0]]
self.assertAllEqual(gradient_values, expected)
