# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
logits = [-42., 42.]
dist = bernoulli.Bernoulli(logits=logits)
self.assertAllClose(logits, self.evaluate(dist.logits))

if not special:
    exit()

self.assertAllClose(special.expit(logits), self.evaluate(dist.probs))

p = [0.01, 0.99, 0.42]
dist = bernoulli.Bernoulli(probs=p)
self.assertAllClose(special.logit(p), self.evaluate(dist.logits))
