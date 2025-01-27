# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
x = constant_op.constant(
    [[np.nan, 0.0], [np.nan, np.inf], [np.inf, np.nan]], name="x")
with self.assertRaises(AssertionError):
    self.assertAllInRange(x, 0.0, 2.0)
