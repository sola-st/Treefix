# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
dist = bernoulli.Bernoulli(probs=1.0)
self.assertAllClose(np.nan, self.evaluate(dist.log_prob(0)))
self.assertAllClose([np.nan], [self.evaluate(dist.log_prob(1))])
