# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
p = [[0.1, 0.2, 0.7], [0.2, 0.3, 0.5]]
n = [[3.], [4]]
with self.cached_session():
    dist = multinomial.Multinomial(total_count=n, probs=p)
    self.assertEqual((2, 1), dist.total_count.get_shape())
    self.assertAllClose(n, dist.total_count)
