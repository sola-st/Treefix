# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = array_ops.placeholder(np.float64, shape=None)
value = du.prefer_static_value(x)
with self.cached_session():
    self.assertAllEqual(np.zeros((2, 3)),
                        value.eval(feed_dict={x: np.zeros((2, 3))}))
