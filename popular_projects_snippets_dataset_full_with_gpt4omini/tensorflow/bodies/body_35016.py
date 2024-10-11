# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = [0.2, 0.4]
dist = bernoulli.Bernoulli(probs=p)
self.assertAllClose(p, self.evaluate(dist.probs))
