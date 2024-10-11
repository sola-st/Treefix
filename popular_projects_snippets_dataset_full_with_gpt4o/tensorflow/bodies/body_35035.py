# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
var = lambda p: p * (1. - p)
p = [[0.2, 0.7], [0.5, 0.4]]
dist = bernoulli.Bernoulli(probs=p)
self.assertAllClose(
    self.evaluate(dist.variance()),
    np.array([[var(0.2), var(0.7)], [var(0.5), var(0.4)]],
             dtype=np.float32))
self.assertAllClose(
    self.evaluate(dist.stddev()),
    np.array([[np.sqrt(var(0.2)), np.sqrt(var(0.7))],
              [np.sqrt(var(0.5)), np.sqrt(var(0.4))]],
             dtype=np.float32))
