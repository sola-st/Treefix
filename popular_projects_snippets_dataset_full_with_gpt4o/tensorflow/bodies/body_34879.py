# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/dirichlet_multinomial_test.py
alpha_v = [1., 2, 3]
alpha_0 = 6.

# Shape [4, 3]
alpha = np.array(4 * [alpha_v], dtype=np.float32)
# Shape [4, 1]
ns = np.array([[2.], [3.], [4.], [5.]], dtype=np.float32)

variance_entry = lambda a, a_sum: a / a_sum * (1 - a / a_sum)
covariance_entry = lambda a, b, a_sum: -a * b / a_sum**2
# Shape [4, 3, 3]
shared_matrix = np.array(
    4 * [[[
        variance_entry(alpha_v[0], alpha_0),
        covariance_entry(alpha_v[0], alpha_v[1], alpha_0),
        covariance_entry(alpha_v[0], alpha_v[2], alpha_0)
    ], [
        covariance_entry(alpha_v[1], alpha_v[0], alpha_0),
        variance_entry(alpha_v[1], alpha_0),
        covariance_entry(alpha_v[1], alpha_v[2], alpha_0)
    ], [
        covariance_entry(alpha_v[2], alpha_v[0], alpha_0),
        covariance_entry(alpha_v[2], alpha_v[1], alpha_0),
        variance_entry(alpha_v[2], alpha_0)
    ]]],
    dtype=np.float32)

with self.cached_session():
    # ns is shape [4, 1], and alpha is shape [4, 3].
    dist = ds.DirichletMultinomial(ns, alpha)
    covariance = dist.covariance()
    expected_covariance = shared_matrix * (
        ns * (ns + alpha_0) / (1 + alpha_0))[..., array_ops.newaxis]

    self.assertEqual([4, 3, 3], covariance.get_shape())
    self.assertAllClose(expected_covariance, self.evaluate(covariance))
