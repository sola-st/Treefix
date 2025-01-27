# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# The probabilities of one vote falling into class k is the mean for class
# k.
with self.cached_session():
    # Both zero-batches.  No broadcast
    alpha = [1., 2]
    counts = [3., 2]
    dist = ds.DirichletMultinomial(5., alpha)
    pmf = dist.prob(counts)
    self.assertAllClose(1 / 7., self.evaluate(pmf))
    self.assertEqual((), pmf.get_shape())
