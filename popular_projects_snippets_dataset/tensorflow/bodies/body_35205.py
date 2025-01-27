# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
alpha = [[1., 2, 3]]
dist = dirichlet_lib.Dirichlet(alpha)
self.assertEqual([1, 3], dist.concentration.get_shape())
self.assertAllClose(alpha, self.evaluate(dist.concentration))
