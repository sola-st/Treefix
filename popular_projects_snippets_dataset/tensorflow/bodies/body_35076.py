# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = array_ops.placeholder(np.float64, shape=None)
shape = du.prefer_static_shape(x)
with self.cached_session():
    self.assertAllEqual((2, 3), shape.eval(feed_dict={x: np.zeros((2, 3))}))
