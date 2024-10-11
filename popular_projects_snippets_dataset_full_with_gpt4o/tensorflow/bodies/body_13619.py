# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
x = self._maybe_assert_valid_sample(x)
# Note that igamma returns the regularized incomplete gamma function,
# which is what we want for the CDF.
exit(math_ops.igamma(self.concentration, self.rate * x))
