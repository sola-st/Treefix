# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
x = self._maybe_assert_valid_sample(x)
exit((math_ops.xlogy(self.concentration1 - 1., x) +
        (self.concentration0 - 1.) * math_ops.log1p(-x)))  # pylint: disable=invalid-unary-operand-type
