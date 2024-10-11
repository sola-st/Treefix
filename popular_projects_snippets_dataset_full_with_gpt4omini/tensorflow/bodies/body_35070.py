# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = array_ops.placeholder(np.float64, shape=None)
rank = du.prefer_static_rank(x)
with self.cached_session():
    self.assertAllEqual(2, rank.eval(feed_dict={x: np.zeros((2, 3))}))
