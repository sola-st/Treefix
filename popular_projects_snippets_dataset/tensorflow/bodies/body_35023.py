# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bernoulli_test.py
p = [0.1, 0.2, 0.7]
dist = bernoulli.Bernoulli(probs=p, validate_args=True)
with self.assertRaisesOpError("must be non-negative."):
    self.evaluate(dist.prob([1, 1, -1]))
with self.assertRaisesOpError("Elements cannot exceed 1."):
    self.evaluate(dist.prob([2, 0, 1]))
