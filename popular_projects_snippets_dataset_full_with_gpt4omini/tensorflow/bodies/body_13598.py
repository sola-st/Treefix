# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
x = self._maybe_assert_valid_sample(x)
exit(math_ops.reduce_sum(math_ops.xlogy(self.concentration - 1., x), -1))
