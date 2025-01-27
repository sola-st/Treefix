# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
alpha = np.random.rand(3, 5, 4).astype(np.float32)
alpha2 = np.random.rand(6, 3, 3).astype(np.float32)

ns = np.random.randint(low=1, high=11, size=[3, 5, 1]).astype(np.float32)
ns2 = np.random.randint(low=1, high=11, size=[6, 1, 1]).astype(np.float32)

with self.cached_session():
    dist = ds.DirichletMultinomial(ns, alpha)
    dist2 = ds.DirichletMultinomial(ns2, alpha2)

    covariance = dist.covariance()
    covariance2 = dist2.covariance()
    self.assertEqual([3, 5, 4, 4], covariance.get_shape())
    self.assertEqual([6, 3, 3, 3], covariance2.get_shape())
