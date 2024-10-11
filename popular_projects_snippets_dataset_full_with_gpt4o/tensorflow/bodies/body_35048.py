# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
p = np.array([[0.3, 0.4, 0.3], [0.1, 0.5, 0.4]], dtype=np.float32)

new_logits, new_p = du.get_logits_and_probs(
    probs=p, multidimensional=True, validate_args=True)

self.assertAllClose(np.log(p), self.evaluate(new_logits))
self.assertAllClose(p, self.evaluate(new_p))
