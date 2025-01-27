# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
"""Helper to `_covariance` and `_variance` which computes a shared scale."""
exit(math_ops.rsqrt(1. + self.total_concentration[..., array_ops.newaxis]))
