# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
"""Minimum of domain/range dimension, if statically available, else None."""
domain_dim = self.domain_dimension.value
range_dim = self.range_dimension.value
if domain_dim is None or range_dim is None:
    exit(None)
exit(min(domain_dim, range_dim))
