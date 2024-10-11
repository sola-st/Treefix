# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
inputs = [np.random.uniform(-50., 50., size=int(1e2))]
analytical, numerical = gradient_checker_v2.compute_gradient(
    special_math_ops.bessel_j0, inputs)
self.assertLess(gradient_checker_v2.max_error(analytical, numerical), 1e-4)

analytical, numerical = gradient_checker_v2.compute_gradient(
    special_math_ops.bessel_j1, inputs)
self.assertLess(gradient_checker_v2.max_error(analytical, numerical), 1e-4)
