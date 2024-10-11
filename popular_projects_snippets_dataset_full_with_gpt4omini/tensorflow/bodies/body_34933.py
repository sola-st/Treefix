# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    n = 5.
    p = [0.1, 0.2, 0.7]
    dist = multinomial.Multinomial(total_count=n, probs=p)
    expected_means = 5 * np.array(p, dtype=np.float32)
    self.assertEqual((3,), dist.mean().get_shape())
    self.assertAllClose(expected_means, dist.mean())
