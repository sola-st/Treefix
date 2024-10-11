# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
with self.cached_session():
    size = ()
    x = constant_op.constant(11 - 13j, dtype=dtypes.complex64)
    y = math_ops.conj(x)
    analytical, numerical = gradient_checker.compute_gradient(x, size, y,
                                                              size)
    correct = np.array([[1, 0], [0, -1]])
    self.assertAllEqual(correct, analytical)
    self.assertAllClose(correct, numerical, rtol=2e-5)
    self.assertLess(
        gradient_checker.compute_gradient_error(x, size, y, size), 2e-5)
