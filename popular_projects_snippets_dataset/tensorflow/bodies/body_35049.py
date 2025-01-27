# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
p = [0.01, 0.2, 0.5, 0.7, .99]
# Component less than 0.
p2 = [-1, 0.2, 0.5, 0.3, .2]
# Component greater than 1.
p3 = [2, 0.2, 0.5, 0.3, .2]

_, prob = du.get_logits_and_probs(probs=p, validate_args=True)
self.evaluate(prob)

with self.assertRaisesOpError("Condition x >= 0"):
    _, prob = du.get_logits_and_probs(probs=p2, validate_args=True)
    self.evaluate(prob)

_, prob = du.get_logits_and_probs(probs=p2, validate_args=False)
self.evaluate(prob)

with self.assertRaisesOpError("probs has components greater than 1"):
    _, prob = du.get_logits_and_probs(probs=p3, validate_args=True)
    self.evaluate(prob)

_, prob = du.get_logits_and_probs(probs=p3, validate_args=False)
self.evaluate(prob)
