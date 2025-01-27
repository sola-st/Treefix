# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    # Shape [2]
    n = [5.] * 2
    # Shape [4, 1, 2]
    p = [[[0.1, 0.9]], [[0.1, 0.9]]] * 2
    dist = multinomial.Multinomial(total_count=n, probs=p)
    # Shape [2, 2]
    inner_var = [[9. / 20, -9 / 20], [-9 / 20, 9 / 20]]
    # Shape [4, 2, 2, 2]
    expected_covariances = [[inner_var, inner_var]] * 4
    self.assertEqual((4, 2, 2, 2), dist.covariance().get_shape())
    self.assertAllClose(expected_covariances, dist.covariance())
