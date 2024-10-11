# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
p = np.array([0.2, 0.3, 0.5], dtype=np.float32)
logits = np.log(p)

new_logits, new_p = du.get_logits_and_probs(
    logits=logits, multidimensional=True, validate_args=True)

self.assertAllClose(self.evaluate(new_p), p)
self.assertAllClose(self.evaluate(new_logits), logits)
