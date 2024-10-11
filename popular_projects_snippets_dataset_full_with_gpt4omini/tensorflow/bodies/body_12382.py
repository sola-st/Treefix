# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/v1_compat_tests/gradient_checker_test.py
with self.cached_session():
    x = array_ops.placeholder(dtypes.float32)
    y = array_ops.identity(x)
    for grad in gradient_checker.compute_gradient(x, (0, 3), y, (0, 3)):
        self.assertEqual(grad.shape, (0, 0))
    error = gradient_checker.compute_gradient_error(x, (0, 3), y, (0, 3))
    self.assertEqual(error, 0)
