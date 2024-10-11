# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
shape = (30, 40, 50)
for dt in (np.float32, np.float64):
    a = 10. * np.random.random(shape).astype(dt)
    b = 10. * np.random.random(shape).astype(dt)
    x = np.random.random(shape).astype(dt)
    actual = self.evaluate(math_ops.exp(beta_lib.Beta(a, b).log_cdf(x)))
    self.assertAllEqual(np.ones(shape, dtype=np.bool_), 0. <= x)
    self.assertAllEqual(np.ones(shape, dtype=np.bool_), 1. >= x)
    if not stats:
        exit()
    self.assertAllClose(stats.beta.cdf(x, a, b), actual, rtol=3e-3, atol=2e-5)
