# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = np.array([1., 2, 3])
dirichlet = dirichlet_lib.Dirichlet(
    concentration=alpha, allow_nan_stats=True)
expected_mode = np.zeros_like(alpha) + np.nan

self.assertEqual(dirichlet.mode().get_shape(), [3])
self.assertAllClose(self.evaluate(dirichlet.mode()), expected_mode)
