# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_test.py
# Test concentration = 1. for each dimension.
concentration = 3 * np.ones((10, 10)).astype(np.float32)
concentration[range(10), range(10)] = 1.
x = 1 / 9. * np.ones((10, 10)).astype(np.float32)
x[range(10), range(10)] = 0.
dist = dirichlet_lib.Dirichlet(concentration)
log_prob = self.evaluate(dist.log_prob(x))
self.assertAllEqual(
    np.ones_like(log_prob, dtype=np.bool_), np.isfinite(log_prob))

# Test when concentration[k] = 1., and x is zero at various dimensions.
dist = dirichlet_lib.Dirichlet(10 * [1.])
log_prob = self.evaluate(dist.log_prob(x))
self.assertAllEqual(
    np.ones_like(log_prob, dtype=np.bool_), np.isfinite(log_prob))
