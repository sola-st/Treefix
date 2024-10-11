# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    n = 5.
    p = [0.1, 0.2, 0.7]
    dist = multinomial.Multinomial(total_count=n, probs=p)
    expected_covariances = [[9. / 20, -1 / 10, -7 / 20],
                            [-1 / 10, 4 / 5, -7 / 10],
                            [-7 / 20, -7 / 10, 21 / 20]]
    self.assertEqual((3, 3), dist.covariance().get_shape())
    self.assertAllClose(expected_covariances, dist.covariance())
