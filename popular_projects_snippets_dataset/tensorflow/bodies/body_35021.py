# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
dist = bernoulli.Bernoulli(**kwargs)
# pylint: disable=bad-continuation
xs = [
    0,
    [1],
    [1, 0],
    [[1, 0]],
    [[1, 0], [1, 1]],
]
expected_pmfs = [
    [[0.8, 0.6], [0.7, 0.4]],
    [[0.2, 0.4], [0.3, 0.6]],
    [[0.2, 0.6], [0.3, 0.4]],
    [[0.2, 0.6], [0.3, 0.4]],
    [[0.2, 0.6], [0.3, 0.6]],
]
# pylint: enable=bad-continuation

for x, expected_pmf in zip(xs, expected_pmfs):
    self.assertAllClose(self.evaluate(dist.prob(x)), expected_pmf)
    self.assertAllClose(self.evaluate(dist.log_prob(x)), np.log(expected_pmf))
