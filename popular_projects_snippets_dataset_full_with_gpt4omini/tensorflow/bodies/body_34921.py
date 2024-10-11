# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
p = np.array([[0.1, 0.2, 0.7]], dtype=np.float32)
logits = np.log(p) - 50.
with self.cached_session():
    multinom = multinomial.Multinomial(total_count=3., logits=logits)
    self.assertEqual((1, 3), multinom.probs.get_shape())
    self.assertEqual((1, 3), multinom.logits.get_shape())
    self.assertAllClose(p, multinom.probs)
    self.assertAllClose(logits, multinom.logits)
