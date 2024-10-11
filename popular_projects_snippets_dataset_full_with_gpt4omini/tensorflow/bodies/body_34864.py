# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
alpha = [[1., 2, 3]]
n = [[5.]]
with self.cached_session():
    dist = ds.DirichletMultinomial(n, alpha)
    self.assertEqual([1, 1], dist.total_count.get_shape())
    self.assertAllClose(n, dist.total_count)
