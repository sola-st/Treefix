# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
# Test with arrays
with self.assertRaises(AssertionError):
    self.assertNotAllClose([1.1, 2.1], [1.0, 2.0], rtol=0.2)

# Test with tensors
x = constant_op.constant([1.0, 1.0], name="x")
y = math_ops.add(x, x)

self.assertAllClose([2.0, 2.0], y)

with self.assertRaises(AssertionError):
    self.assertNotAllClose([0.9, 1.0], x, rtol=0.2)
