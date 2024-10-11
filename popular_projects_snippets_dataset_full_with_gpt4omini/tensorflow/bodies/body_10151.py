# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py

for dtype in [dtypes.float32, dtypes.float64]:
    one = constant_op.constant([1, 1], dtype=dtype)
    two = constant_op.constant([2], dtype=dtype)

    eps = np.finfo(dtype.as_numpy_dtype).eps

    eps_const = constant_op.constant([eps, eps], dtype=dtype)

    self.assertAllEqual(math_ops.nextafter(one, two) - one, eps_const)
