# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
x = constant_op.constant([10.0, np.inf], name="x")
self.assertAllInRange(x, 10, np.inf)
with self.assertRaises(AssertionError):
    self.assertAllInRange(x, 10, np.inf, open_upper_bound=True)
