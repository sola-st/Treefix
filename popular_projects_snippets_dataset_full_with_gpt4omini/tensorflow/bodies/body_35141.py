# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
alpha_v = 4.0
beta_v = 3.0
alpha = constant_op.constant(alpha_v)
beta = constant_op.constant(beta_v)
n = 100000
gamma = gamma_lib.Gamma(concentration=alpha, rate=beta)
samples = gamma.sample(n, seed=137)
sample_values = self.evaluate(samples)
self.assertEqual(samples.get_shape(), (n,))
self.assertEqual(sample_values.shape, (n,))
self.assertTrue(self._kstest(alpha_v, beta_v, sample_values))
if not stats:
    exit()
self.assertAllClose(
    sample_values.mean(),
    stats.gamma.mean(alpha_v, scale=1 / beta_v),
    atol=.01)
self.assertAllClose(
    sample_values.var(),
    stats.gamma.var(alpha_v, scale=1 / beta_v),
    atol=.15)
