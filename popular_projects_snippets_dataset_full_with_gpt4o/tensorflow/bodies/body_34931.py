# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    # [2, 2, 2]
    p = [[[0.1, 0.9], [0.1, 0.9]], [[0.7, 0.3], [0.7, 0.3]]]
    # [2, 2]
    n = [[3., 3], [3, 3]]
    # [2]
    counts = [2., 1]
    pmf = multinomial.Multinomial(total_count=n, probs=p).prob(counts)
    self.evaluate(pmf)
    self.assertEqual(pmf.get_shape(), (2, 2))
