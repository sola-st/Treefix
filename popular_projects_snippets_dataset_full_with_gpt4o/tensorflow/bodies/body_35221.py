# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = [1., 2, 3]
dirichlet = dirichlet_lib.Dirichlet(concentration=alpha)
self.assertEqual(dirichlet.entropy().get_shape(), ())
if not stats:
    exit()
expected_entropy = stats.dirichlet.entropy(alpha)
self.assertAllClose(self.evaluate(dirichlet.entropy()), expected_entropy)
