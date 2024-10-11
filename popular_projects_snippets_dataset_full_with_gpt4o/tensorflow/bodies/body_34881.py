# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# There is only one way for zero items to be selected, and this happens with
# probability 1.
alpha = [5, 0.5]
counts = [0., 0]
with self.cached_session():
    dist = ds.DirichletMultinomial(0., alpha)
    pmf = dist.prob(counts)
    self.assertAllClose(1.0, self.evaluate(pmf))
    self.assertEqual((), pmf.get_shape())
