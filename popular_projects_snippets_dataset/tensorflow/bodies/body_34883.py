# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# If tau is small, then correlation between draws is large, so draws that
# are both of the same class are more likely.
mu = np.array([0.5, 0.5], dtype=np.float32)
tau = np.array([0.1], dtype=np.float32)
alpha = tau * mu

# If there is only one draw, it is still a coin flip, even with small tau.
counts = [1., 0]
with self.cached_session():
    dist = ds.DirichletMultinomial(1., alpha)
    pmf = dist.prob(counts)
    self.assertAllClose(0.5, self.evaluate(pmf))
    self.assertEqual((), pmf.get_shape())

# If there are two draws, it is much more likely that they are the same.
counts_same = [2., 0]
counts_different = [1, 1.]
with self.cached_session():
    dist = ds.DirichletMultinomial(2., alpha)
    pmf_same = dist.prob(counts_same)
    pmf_different = dist.prob(counts_different)
    self.assertLess(5 * self.evaluate(pmf_different), self.evaluate(pmf_same))
    self.assertEqual((), pmf_same.get_shape())
