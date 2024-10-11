# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
param_shapes = normal_lib.Normal.param_shapes(sample_shape)
mu_shape, sigma_shape = param_shapes["loc"], param_shapes["scale"]
self.assertAllEqual(expected, self.evaluate(mu_shape))
self.assertAllEqual(expected, self.evaluate(sigma_shape))
mu = array_ops.zeros(mu_shape)
sigma = array_ops.ones(sigma_shape)
self.assertAllEqual(
    expected,
    self.evaluate(array_ops.shape(normal_lib.Normal(mu, sigma).sample())))
