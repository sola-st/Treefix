# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
p = np.array([[0.3, 0.4, 0.3], [0.1, 0.5, 0.4]], dtype=np.float32)
# Component less than 0. Still sums to 1.
p2 = np.array([[-.3, 0.4, 0.9], [0.1, 0.5, 0.4]], dtype=np.float32)
# Component greater than 1. Does not sum to 1.
p3 = np.array([[1.3, 0.0, 0.0], [0.1, 0.5, 0.4]], dtype=np.float32)
# Does not sum to 1.
p4 = np.array([[1.1, 0.3, 0.4], [0.1, 0.5, 0.4]], dtype=np.float32)

_, prob = du.get_logits_and_probs(probs=p, multidimensional=True)
self.evaluate(prob)

with self.assertRaisesOpError("Condition x >= 0"):
    _, prob = du.get_logits_and_probs(
        probs=p2, multidimensional=True, validate_args=True)
    self.evaluate(prob)

_, prob = du.get_logits_and_probs(
    probs=p2, multidimensional=True, validate_args=False)
self.evaluate(prob)

with self.assertRaisesOpError(
    "(probs has components greater than 1|probs does not sum to 1)"):
    _, prob = du.get_logits_and_probs(
        probs=p3, multidimensional=True, validate_args=True)
    self.evaluate(prob)

_, prob = du.get_logits_and_probs(
    probs=p3, multidimensional=True, validate_args=False)
self.evaluate(prob)

with self.assertRaisesOpError("probs does not sum to 1"):
    _, prob = du.get_logits_and_probs(
        probs=p4, multidimensional=True, validate_args=True)
    self.evaluate(prob)

_, prob = du.get_logits_and_probs(
    probs=p4, multidimensional=True, validate_args=False)
self.evaluate(prob)
