# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/exponential_test.py
lam = constant_op.constant([3.0, 4.0])
lam_v = [3.0, 4.0]
n = constant_op.constant(100000)
exponential = exponential_lib.Exponential(rate=lam)

samples = exponential.sample(n, seed=137)
sample_values = self.evaluate(samples)
self.assertEqual(sample_values.shape, (100000, 2))
self.assertFalse(np.any(sample_values < 0.0))
if not stats:
    exit()
for i in range(2):
    self.assertLess(
        stats.kstest(sample_values[:, i],
                     stats.expon(scale=1.0 / lam_v[i]).cdf)[0], 0.01)
