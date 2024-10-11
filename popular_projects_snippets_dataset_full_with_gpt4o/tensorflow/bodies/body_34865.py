# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
alpha = [[1., 2, 3]]
with self.cached_session():
    dist = ds.DirichletMultinomial(1, alpha)
    self.assertEqual([1, 3], dist.concentration.get_shape())
    self.assertAllClose(alpha, dist.concentration)
