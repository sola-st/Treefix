# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
p = np.array([0.01, 0.2, 0.5, 0.7, .99], dtype=np.float32)

new_logits, new_p = du.get_logits_and_probs(probs=p, validate_args=True)

self.assertAllClose(_logit(p), self.evaluate(new_logits))
self.assertAllClose(p, self.evaluate(new_p))
