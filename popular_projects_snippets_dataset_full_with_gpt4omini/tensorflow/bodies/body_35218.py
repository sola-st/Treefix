# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = np.array([1.1, 2, 3])
expected_mode = (alpha - 1) / (np.sum(alpha) - 3)
dirichlet = dirichlet_lib.Dirichlet(concentration=alpha)
self.assertEqual(dirichlet.mode().get_shape(), [3])
self.assertAllClose(self.evaluate(dirichlet.mode()), expected_mode)
