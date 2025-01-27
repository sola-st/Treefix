# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
a = array_ops.constant([2], dtype=dtypes.int32)
# Since __future__.division is effect, we should always upgrade to float64
b = math_ops.divide(a, 1)
self.assertEqual(b.dtype, dtypes.float64)
self.assertEqual(2.0, self.evaluate(b))
c = math_ops.divide(a, 4)
self.assertEqual(c.dtype, dtypes.float64)
self.assertEqual(0.5, self.evaluate(c))
