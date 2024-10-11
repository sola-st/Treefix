# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
# Test with arrays
self.assertNotAllClose([0.1], [0.2])
with self.assertRaises(AssertionError):
    self.assertNotAllClose([-1.0, 2.0], [-1.0, 2.0])

# Test with tensors
x = constant_op.constant([1.0, 1.0], name="x")
y = math_ops.add(x, x)

self.assertAllClose([2.0, 2.0], y)
self.assertNotAllClose([0.9, 1.0], x)

with self.assertRaises(AssertionError):
    self.assertNotAllClose([1.0, 1.0], x)
