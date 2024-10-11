# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
x = constant_op.constant([100.0, 110.0, 120.0], dtype=dtypes.float32)
y = constant_op.constant([10.0] * 3, dtype=dtypes.float32)
z = math_ops.add(x, y)

self.assertAllEqual([110.0, 120.0, 130.0], z)

self.assertAllGreaterEqual(x, 95.0)
self.assertAllLessEqual(x, 125.0)

with self.assertRaises(AssertionError):
    self.assertAllGreaterEqual(x, 105.0)
with self.assertRaises(AssertionError):
    self.assertAllGreaterEqual(x, 125.0)

with self.assertRaises(AssertionError):
    self.assertAllLessEqual(x, 115.0)
with self.assertRaises(AssertionError):
    self.assertAllLessEqual(x, 95.0)
