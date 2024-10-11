# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    p = [0.1, 0.9]
    counts = [[1., 0], [0, 1]]
    pmf = multinomial.Multinomial(total_count=1., probs=p).prob(counts)
    self.assertAllClose([0.1, 0.9], self.evaluate(pmf))
    self.assertEqual((2), pmf.get_shape())
