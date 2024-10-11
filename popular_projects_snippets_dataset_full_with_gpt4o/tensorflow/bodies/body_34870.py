# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# The probabilities of one vote falling into class k is the mean for class
# k.
with self.cached_session():
    alpha = [1., 2]
    counts = [3., 2]
    n = np.full([4, 3], 5., dtype=np.float32)
    dist = ds.DirichletMultinomial(n, alpha)
    pmf = dist.prob(counts)
    self.assertAllClose([[1 / 7., 1 / 7., 1 / 7.]] * 4, self.evaluate(pmf))
    self.assertEqual((4, 3), pmf.get_shape())
