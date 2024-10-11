# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
# Shape [3, 5, 4]
p = np.random.dirichlet([.25, .25, .25, .25], [3, 5]).astype(np.float32)
# Shape [6, 3, 3]
p2 = np.random.dirichlet([.3, .3, .4], [6, 3]).astype(np.float32)

ns = np.random.randint(low=1, high=11, size=[3, 5]).astype(np.float32)
ns2 = np.random.randint(low=1, high=11, size=[6, 1]).astype(np.float32)

with self.cached_session():
    dist = multinomial.Multinomial(ns, p)
    dist2 = multinomial.Multinomial(ns2, p2)

    covariance = dist.covariance()
    covariance2 = dist2.covariance()
    self.assertEqual((3, 5, 4, 4), covariance.get_shape())
    self.assertEqual((6, 3, 3, 3), covariance2.get_shape())
