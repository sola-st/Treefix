# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# The probabilities of one vote falling into class k is the mean for class
# k.
with self.cached_session():
    alpha = [[1., 2], [2., 3]]
    counts = [[1., 0]]
    pmf = ds.DirichletMultinomial([1., 1.], alpha).prob(counts)
    self.assertAllClose([1 / 3., 2 / 5.], self.evaluate(pmf))
    self.assertAllEqual([2], pmf.get_shape())
