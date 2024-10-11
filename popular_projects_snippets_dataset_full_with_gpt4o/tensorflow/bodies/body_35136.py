# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/gamma_test.py
# Mode will not be defined for the first entry.
alpha_v = np.array([0.5, 3.0, 2.5])
beta_v = np.array([1.0, 4.0, 5.0])
gamma = gamma_lib.Gamma(
    concentration=alpha_v, rate=beta_v, allow_nan_stats=True)
expected_modes = (alpha_v - 1) / beta_v
expected_modes[0] = np.nan
self.assertEqual(gamma.mode().get_shape(), (3,))
self.assertAllClose(self.evaluate(gamma.mode()), expected_modes)
