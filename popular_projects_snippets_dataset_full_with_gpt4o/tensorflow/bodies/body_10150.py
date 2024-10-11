# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py

for dtype in [dtypes.float32, dtypes.float64]:
    one = constant_op.constant([1], dtype=dtype)
    two = constant_op.constant([2], dtype=dtype)
    zero = constant_op.constant([0], dtype=dtype)
    nan = constant_op.constant([np.nan], dtype=dtype)

    eps = constant_op.constant([np.finfo(dtype.as_numpy_dtype).eps],
                               dtype=dtype)

    self.assertAllEqual(math_ops.nextafter(one, two) - one, eps)
    self.assertAllLess(math_ops.nextafter(one, zero) - one, 0)
    self.assertAllEqual(math_ops.is_nan(math_ops.nextafter(nan, one)), [True])
    self.assertAllEqual(math_ops.is_nan(math_ops.nextafter(one, nan)), [True])
    self.assertAllEqual(math_ops.nextafter(one, one), one)
