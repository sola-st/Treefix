# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = 0.2
dist = bernoulli.Bernoulli(probs=p)
self.assertAllClose(self.evaluate(dist.entropy()), entropy(p))
