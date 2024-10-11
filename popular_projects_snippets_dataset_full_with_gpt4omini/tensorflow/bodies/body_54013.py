# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
x = constant_op.constant(10.0, name="x")
nan = constant_op.constant(np.nan, name="nan")
self.assertAllInRange(x, 5, 15)
with self.assertRaises(AssertionError):
    self.assertAllInRange(nan, 5, 15)

with self.assertRaises(AssertionError):
    self.assertAllInRange(x, 10, 15, open_lower_bound=True)
with self.assertRaises(AssertionError):
    self.assertAllInRange(x, 1, 2)
