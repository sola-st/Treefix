# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = [[0.1, 0.7], [0.2, 0.6]]
dist = bernoulli.Bernoulli(probs=p, validate_args=False)
self.assertAllClose(
    self.evaluate(dist.entropy()),
    [[entropy(0.1), entropy(0.7)], [entropy(0.2),
                                    entropy(0.6)]])
