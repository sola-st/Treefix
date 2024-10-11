# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
with self.cached_session():
    x = array_ops.zeros([0, 3])
    y = math_ops.reduce_min(x, [1])
    error = gradient_checker.compute_gradient_error(x, [0, 3], y, [0])
    self.assertEqual(error, 0)
