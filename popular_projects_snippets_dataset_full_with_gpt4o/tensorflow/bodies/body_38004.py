# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
with self.cached_session():
    for dtype in (np.float16, np.float32, np.float64, np.complex64,
                  np.complex128):
        x = constant_op.constant(0.0, dtype=dtype)
        y = constant_op.constant(2.0, dtype=dtype)
        z = math_ops.pow(x, y)
        error = gradient_checker.compute_gradient_error(y, [], z, [])
        self.assertEqual(error, 0)
