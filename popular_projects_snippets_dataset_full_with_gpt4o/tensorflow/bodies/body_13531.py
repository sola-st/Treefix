# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
exit((
    self._log_normalization()
    - (self.concentration1 - 1.) * math_ops.digamma(self.concentration1)
    - (self.concentration0 - 1.) * math_ops.digamma(self.concentration0)
    + ((self.total_concentration - 2.) *
       math_ops.digamma(self.total_concentration))))
