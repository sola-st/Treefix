# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# The probabilities of one vote falling into class k is the mean for class
# k.
with self.cached_session():
    alpha = [[1., 2]]
    counts = [[1., 0], [0., 1]]
    dist = ds.DirichletMultinomial([1.], alpha)
    pmf = dist.prob(counts)
    self.assertAllClose([1 / 3., 2 / 3.], self.evaluate(pmf))
    self.assertAllEqual([2], pmf.get_shape())
