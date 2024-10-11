# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
x = constant_op.constant([10.0, 15.0], name="x")
self.assertAllInRange(x, 10, 15)

with self.assertRaises(AssertionError):
    self.assertAllInRange(x, 10, 15, open_lower_bound=True)
with self.assertRaises(AssertionError):
    self.assertAllInRange(x, 10, 15, open_upper_bound=True)
with self.assertRaises(AssertionError):
    self.assertAllInRange(
        x, 10, 15, open_lower_bound=True, open_upper_bound=True)
