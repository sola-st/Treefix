# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = [1., 2, 3]
denominator = np.sum(alpha)**2 * (np.sum(alpha) + 1)
dirichlet = dirichlet_lib.Dirichlet(concentration=alpha)
self.assertEqual(dirichlet.covariance().get_shape(), (3, 3))
if not stats:
    exit()
expected_covariance = np.diag(stats.dirichlet.var(alpha))
expected_covariance += [[0., -2, -3], [-2, 0, -6], [-3, -6, 0]
                       ] / denominator
self.assertAllClose(
    self.evaluate(dirichlet.covariance()), expected_covariance)
