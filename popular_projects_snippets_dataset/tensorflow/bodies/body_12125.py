# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
inputs = [np.random.uniform(1., 50., size=int(1e2))]
analytical, numerical = gradient_checker_v2.compute_gradient(
    special_math_ops.fresnel_cos, inputs)
self.assertLess(gradient_checker_v2.max_error(analytical, numerical), 5e-3)
