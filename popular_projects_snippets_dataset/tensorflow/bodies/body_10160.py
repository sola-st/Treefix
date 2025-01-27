# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
x = constant_op.constant([1.0, 2.0, 0.0, 4.0], dtype=dtypes.float32)
self.assertNotEqual(x, None)
self.assertNotEqual(None, x)
self.assertFalse(math_ops.tensor_equals(x, None))
self.assertTrue(math_ops.tensor_not_equals(x, None))
