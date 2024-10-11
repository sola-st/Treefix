# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/exponential_test.py
lam = [-2.2, -3.4]
exponential = exponential_lib.ExponentialWithSoftplusRate(rate=lam)
self.assertAllClose(
    self.evaluate(nn_ops.softplus(lam)), self.evaluate(exponential.rate))
