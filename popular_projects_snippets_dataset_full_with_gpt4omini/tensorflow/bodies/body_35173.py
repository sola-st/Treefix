# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = 1.
b = 2.
beta = beta_lib.Beta(a, b)
n = constant_op.constant(100000)
samples = beta.sample(n)
sample_values = self.evaluate(samples)
self.assertEqual(sample_values.shape, (100000,))
self.assertFalse(np.any(sample_values < 0.0))
if not stats:
    exit()
self.assertLess(
    stats.kstest(
        # Beta is a univariate distribution.
        sample_values,
        stats.beta(a=1., b=2.).cdf)[0],
    0.01)
# The standard error of the sample mean is 1 / (sqrt(18 * n))
self.assertAllClose(
    sample_values.mean(axis=0), stats.beta.mean(a, b), atol=1e-2)
self.assertAllClose(
    np.cov(sample_values, rowvar=0), stats.beta.var(a, b), atol=1e-1)
