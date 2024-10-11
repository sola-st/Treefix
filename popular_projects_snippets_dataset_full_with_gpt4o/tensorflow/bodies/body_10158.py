# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in self.allowed_dtypes:
    x = constant_op.constant([1.0, 2.0, 0.0, 4.0], dtype=dtype)

    y = math_ops.reciprocal_no_nan(x)

    target = constant_op.constant([1.0, 0.5, 0.0, 0.25], dtype=dtype)

    self.assertAllEqual(y, target)
    self.assertEqual(y.dtype.base_dtype, target.dtype.base_dtype)
