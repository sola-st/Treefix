# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
param_shapes = normal_lib.Normal.param_static_shapes(sample_shape)
mu_shape, sigma_shape = param_shapes["loc"], param_shapes["scale"]
self.assertEqual(expected, mu_shape)
self.assertEqual(expected, sigma_shape)
