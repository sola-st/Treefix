# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
p = [[0.1, 0.2, 0.7]]
with self.cached_session():
    dist = multinomial.Multinomial(total_count=3., probs=p)
    self.assertEqual((1, 3), dist.probs.get_shape())
    self.assertEqual((1, 3), dist.logits.get_shape())
    self.assertAllClose(p, dist.probs)
