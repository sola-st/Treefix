# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
batch_size = 6
mu_a = np.array([3.0] * batch_size)
sigma_a = np.array([1.0, 2.0, 3.0, 1.5, 2.5, 3.5])
mu_b = np.array([-3.0] * batch_size)
sigma_b = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])

n_a = normal_lib.Normal(loc=mu_a, scale=sigma_a)
n_b = normal_lib.Normal(loc=mu_b, scale=sigma_b)

kl = kullback_leibler.kl_divergence(n_a, n_b)
kl_val = self.evaluate(kl)

kl_expected = ((mu_a - mu_b)**2 / (2 * sigma_b**2) + 0.5 * (
    (sigma_a**2 / sigma_b**2) - 1 - 2 * np.log(sigma_a / sigma_b)))

self.assertEqual(kl.get_shape(), (batch_size,))
self.assertAllClose(kl_val, kl_expected)
