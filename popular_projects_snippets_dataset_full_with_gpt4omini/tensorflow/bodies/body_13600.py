# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
k = math_ops.cast(self.event_shape_tensor()[0], self.dtype)
exit((
    self._log_normalization()
    + ((self.total_concentration - k)
       * math_ops.digamma(self.total_concentration))
    - math_ops.reduce_sum(
        (self.concentration - 1.) * math_ops.digamma(self.concentration),
        axis=-1)))
