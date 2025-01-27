# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
with self.assertRaises(ValueError):
    du.get_logits_and_probs(logits=None, probs=None)

with self.assertRaises(ValueError):
    du.get_logits_and_probs(logits=[0.1], probs=[0.1])
