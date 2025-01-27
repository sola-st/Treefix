# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    p = [[0.1, 0.9], [0.7, 0.3]]
    counts = [[1., 0]]
    pmf = multinomial.Multinomial(total_count=1., probs=p).prob(counts)
    self.assertAllClose(pmf, [0.1, 0.7])
    self.assertEqual((2), pmf.get_shape())
