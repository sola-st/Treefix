# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = [1., 2, 3]
dirichlet = dirichlet_lib.Dirichlet(concentration=alpha)
self.assertEqual(dirichlet.mean().get_shape(), [3])
if not stats:
    exit()
expected_mean = stats.dirichlet.mean(alpha)
self.assertAllClose(self.evaluate(dirichlet.mean()), expected_mean)
