# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = [[0.2, 0.4], [0.3, 0.6]]
self._testPmf(probs=p)
if not special:
    exit()
self._testPmf(logits=special.logit(p))
