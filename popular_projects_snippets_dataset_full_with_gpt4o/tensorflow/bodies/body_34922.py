# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/multinomial_test.py
logits = np.array([[-200, 0]], dtype=np.float32)
with self.cached_session():
    dist = multinomial.Multinomial(total_count=1., logits=logits)
    lp = dist.log_prob([1., 0.]).eval()[0]
    self.assertAllClose(-200, lp, atol=0, rtol=1e-6)
