# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
for dtype in self.allowed_dtypes:
    x = np.random.choice([0, 1, 2, 4, 5], size=(5, 5, 5))
    x = constant_op.constant(x, dtype=dtype)

    y = math_ops.reciprocal_no_nan(math_ops.reciprocal_no_nan(x))

    self.assertAllClose(y, x)
    self.assertEqual(y.dtype.base_dtype, x.dtype.base_dtype)
