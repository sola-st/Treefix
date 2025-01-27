# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
# Shape [2]
alpha = [1., 2]
ns = [2., 3., 4., 5.]
alpha_0 = np.sum(alpha)

# Diagonal entries are of the form:
# Var(X_i) = n * alpha_i / alpha_sum * (1 - alpha_i / alpha_sum) *
# (alpha_sum + n) / (alpha_sum + 1)
variance_entry = lambda a, a_sum: a / a_sum * (1 - a / a_sum)
# Off diagonal entries are of the form:
# Cov(X_i, X_j) = -n * alpha_i * alpha_j / (alpha_sum ** 2) *
# (alpha_sum + n) / (alpha_sum + 1)
covariance_entry = lambda a, b, a_sum: -a * b / a_sum**2
# Shape [2, 2].
shared_matrix = np.array([[
    variance_entry(alpha[0], alpha_0),
    covariance_entry(alpha[0], alpha[1], alpha_0)
], [
    covariance_entry(alpha[1], alpha[0], alpha_0),
    variance_entry(alpha[1], alpha_0)
]])

with self.cached_session():
    for n in ns:
        # n is shape [] and alpha is shape [2].
        dist = ds.DirichletMultinomial(n, alpha)
        covariance = dist.covariance()
        expected_covariance = n * (n + alpha_0) / (1 + alpha_0) * shared_matrix

        self.assertEqual([2, 2], covariance.get_shape())
        self.assertAllClose(expected_covariance, self.evaluate(covariance))
