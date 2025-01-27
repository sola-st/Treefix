# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
loc_v = np.array([np.arange(1, 101, dtype=np.float32)])  # 1 x 100
scale_v = np.array([np.arange(1, 11, dtype=np.float32)]).T  # 10 x 1
laplace = laplace_lib.Laplace(loc=loc_v, scale=scale_v)
n = 10000
samples = laplace.sample(n, seed=137)
sample_values = self.evaluate(samples)
self.assertEqual(samples.get_shape(), (n, 10, 100))
self.assertEqual(sample_values.shape, (n, 10, 100))
zeros = np.zeros_like(loc_v + scale_v)  # 10 x 100
loc_bc = loc_v + zeros
scale_bc = scale_v + zeros
if not stats:
    exit()
self.assertAllClose(
    sample_values.mean(axis=0),
    stats.laplace.mean(loc_bc, scale=scale_bc),
    rtol=0.35,
    atol=0.)
self.assertAllClose(
    sample_values.var(axis=0),
    stats.laplace.var(loc_bc, scale=scale_bc),
    rtol=0.105,
    atol=0.0)
fails = 0
trials = 0
for ai, a in enumerate(np.reshape(loc_v, [-1])):
    for bi, b in enumerate(np.reshape(scale_v, [-1])):
        s = sample_values[:, bi, ai]
        trials += 1
        fails += 0 if self._kstest(a, b, s) else 1
self.assertLess(fails, trials * 0.03)
