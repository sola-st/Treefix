# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
with self.cached_session():
    size = ()
    c = constant_op.constant(5 + 7j, dtype=dtypes.complex64)
    x = constant_op.constant(11 - 13j, dtype=dtypes.complex64)
    y = c * x
    analytical, numerical = gradient_checker.compute_gradient(x, size, y,
                                                              size)
    correct = np.array([[5, 7], [-7, 5]])
    self.assertAllEqual(correct, analytical)
    self.assertAllClose(correct, numerical, rtol=1e-4)
    self.assertLess(
        gradient_checker.compute_gradient_error(x, size, y, size), 3e-4)
