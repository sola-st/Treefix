# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
alpha_v = constant_op.constant([0.0, -2.1], name="alpha")
beta_v = constant_op.constant([1.0, -3.6], name="beta")
gamma = gamma_lib.GammaWithSoftplusConcentrationRate(
    concentration=alpha_v, rate=beta_v)
self.assertAllEqual(
    self.evaluate(nn_ops.softplus(alpha_v)),
    self.evaluate(gamma.concentration))
self.assertAllEqual(
    self.evaluate(nn_ops.softplus(beta_v)), self.evaluate(gamma.rate))
