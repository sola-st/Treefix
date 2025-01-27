# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = [1., 2]
dirichlet = dirichlet_lib.Dirichlet(alpha)
n = constant_op.constant(100000)
samples = dirichlet.sample(n)
sample_values = self.evaluate(samples)
self.assertEqual(sample_values.shape, (100000, 2))
self.assertTrue(np.all(sample_values > 0.0))
if not stats:
    exit()
self.assertLess(
    stats.kstest(
        # Beta is a univariate distribution.
        sample_values[:, 0],
        stats.beta(a=1., b=2.).cdf)[0],
    0.01)
