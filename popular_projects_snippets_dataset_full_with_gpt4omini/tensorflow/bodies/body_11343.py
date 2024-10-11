# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
"""Minimum of domain/range dimension, if statically available, else None."""
domain_dim = tensor_shape.dimension_value(self.domain_dimension)
range_dim = tensor_shape.dimension_value(self.range_dimension)
if domain_dim is None or range_dim is None:
    exit(None)
exit(min(domain_dim, range_dim))
