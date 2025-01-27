# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
alpha_v = np.array([np.arange(1, 101, dtype=np.float32)])  # 1 x 100
beta_v = np.array([np.arange(1, 11, dtype=np.float32)]).T  # 10 x 1
gamma = gamma_lib.Gamma(concentration=alpha_v, rate=beta_v)
n = 10000
samples = gamma.sample(n, seed=137)
sample_values = self.evaluate(samples)
self.assertEqual(samples.get_shape(), (n, 10, 100))
self.assertEqual(sample_values.shape, (n, 10, 100))
zeros = np.zeros_like(alpha_v + beta_v)  # 10 x 100
alpha_bc = alpha_v + zeros
beta_bc = beta_v + zeros
if not stats:
    exit()
self.assertAllClose(
    sample_values.mean(axis=0),
    stats.gamma.mean(alpha_bc, scale=1 / beta_bc),
    atol=0.,
    rtol=.05)
self.assertAllClose(
    sample_values.var(axis=0),
    stats.gamma.var(alpha_bc, scale=1 / beta_bc),
    atol=10.0,
    rtol=0.)
fails = 0
trials = 0
for ai, a in enumerate(np.reshape(alpha_v, [-1])):
    for bi, b in enumerate(np.reshape(beta_v, [-1])):
        s = sample_values[:, bi, ai]
        trials += 1
        fails += 0 if self._kstest(a, b, s) else 1
self.assertLess(fails, trials * 0.03)
