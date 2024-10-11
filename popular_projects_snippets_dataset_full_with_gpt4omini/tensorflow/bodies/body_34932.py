# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
with self.cached_session():
    p = [0.1, 0.9]
    counts = [3., 2]
    n = np.full([4, 3], 5., dtype=np.float32)
    pmf = multinomial.Multinomial(total_count=n, probs=p).prob(counts)
    self.evaluate(pmf)
    self.assertEqual((4, 3), pmf.get_shape())
