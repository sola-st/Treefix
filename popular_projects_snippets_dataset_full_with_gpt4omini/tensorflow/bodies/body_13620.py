# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
x = self._maybe_assert_valid_sample(x)
exit(math_ops.xlogy(self.concentration - 1., x) - self.rate * x)
