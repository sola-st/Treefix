# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
p = np.array([0.01, 0.2, 0.5, 0.7, .99], dtype=np.float32)
logits = _logit(p)

new_logits, new_p = du.get_logits_and_probs(
    logits=logits, validate_args=True)

self.assertAllClose(p, self.evaluate(new_p), rtol=1e-5, atol=0.)
self.assertAllClose(logits, self.evaluate(new_logits), rtol=1e-5, atol=0.)
