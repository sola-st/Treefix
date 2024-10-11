# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
# Test case for https://github.com/tensorflow/tensorflow/issues/39475
x = math_ops.divide(5, 2)
self.assertIsInstance(x, ops.Tensor)
x = math_ops.divide(5, array_ops.constant(2.0))
self.assertIsInstance(x, ops.Tensor)
