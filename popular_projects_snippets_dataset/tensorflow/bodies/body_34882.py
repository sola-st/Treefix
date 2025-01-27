# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# If tau is large, we are doing coin flips with probability mu.
mu = np.array([0.1, 0.1, 0.8], dtype=np.float32)
tau = np.array([100.], dtype=np.float32)
alpha = tau * mu

# One (three sided) coin flip.  Prob[coin 3] = 0.8.
# Note that since it was one flip, value of tau didn't matter.
counts = [0., 0, 1]
with self.cached_session():
    dist = ds.DirichletMultinomial(1., alpha)
    pmf = dist.prob(counts)
    self.assertAllClose(0.8, self.evaluate(pmf), atol=1e-4)
    self.assertEqual((), pmf.get_shape())

# Two (three sided) coin flips.  Prob[coin 3] = 0.8.
counts = [0., 0, 2]
with self.cached_session():
    dist = ds.DirichletMultinomial(2., alpha)
    pmf = dist.prob(counts)
    self.assertAllClose(0.8**2, self.evaluate(pmf), atol=1e-2)
    self.assertEqual((), pmf.get_shape())

# Three (three sided) coin flips.
counts = [1., 0, 2]
with self.cached_session():
    dist = ds.DirichletMultinomial(3., alpha)
    pmf = dist.prob(counts)
    self.assertAllClose(3 * 0.1 * 0.8 * 0.8, self.evaluate(pmf), atol=1e-2)
    self.assertEqual((), pmf.get_shape())
