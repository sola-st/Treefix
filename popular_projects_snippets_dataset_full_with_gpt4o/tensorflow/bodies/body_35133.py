# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
alpha_v = np.array([1.0, 3.0, 2.5])
beta_v = np.array([1.0, 4.0, 5.0])
gamma = gamma_lib.Gamma(concentration=alpha_v, rate=beta_v)
self.assertEqual(gamma.mean().get_shape(), (3,))
if not stats:
    exit()
expected_means = stats.gamma.mean(alpha_v, scale=1 / beta_v)
self.assertAllClose(self.evaluate(gamma.mean()), expected_means)
