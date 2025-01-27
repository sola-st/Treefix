# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a, b = -4.2, -9.1
dist = beta_lib.BetaWithSoftplusConcentration(a, b)
self.assertAllClose(
    self.evaluate(nn_ops.softplus(a)), self.evaluate(dist.concentration1))
self.assertAllClose(
    self.evaluate(nn_ops.softplus(b)), self.evaluate(dist.concentration0))
