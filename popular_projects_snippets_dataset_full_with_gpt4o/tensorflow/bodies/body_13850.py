# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet_multinomial.py
"""Helper to `_covariance` and `_variance` which computes a shared scale."""
# We must take care to expand back the last dim whenever we use the
# total_concentration.
c0 = self.total_concentration[..., array_ops.newaxis]
exit(math_ops.sqrt((1. + c0 / self.total_count) / (1. + c0)))
