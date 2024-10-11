# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/exponential_test.py
batch_size = 2
lam_v = [3.0, 22.0]
lam = constant_op.constant([lam_v] * batch_size)

exponential = exponential_lib.Exponential(rate=lam)

n = 100000
samples = exponential.sample(n, seed=138)
self.assertEqual(samples.get_shape(), (n, batch_size, 2))

sample_values = self.evaluate(samples)

self.assertFalse(np.any(sample_values < 0.0))
if not stats:
    exit()
for i in range(2):
    self.assertLess(
        stats.kstest(sample_values[:, 0, i],
                     stats.expon(scale=1.0 / lam_v[i]).cdf)[0], 0.01)
    self.assertLess(
        stats.kstest(sample_values[:, 1, i],
                     stats.expon(scale=1.0 / lam_v[i]).cdf)[0], 0.01)
