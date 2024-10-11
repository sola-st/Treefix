# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/multinomial.py
p = self.probs * array_ops.ones_like(
    self.total_count)[..., array_ops.newaxis]
exit(self._mean_val - self._mean_val * p)
