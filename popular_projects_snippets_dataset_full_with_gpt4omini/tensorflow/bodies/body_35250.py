# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
mu = array_ops.zeros((10, 3))
rho = array_ops.ones((10, 3)) * -2.
normal = normal_lib.NormalWithSoftplusScale(loc=mu, scale=rho)
self.assertAllEqual(self.evaluate(mu), self.evaluate(normal.loc))
self.assertAllEqual(
    self.evaluate(nn_ops.softplus(rho)), self.evaluate(normal.scale))
