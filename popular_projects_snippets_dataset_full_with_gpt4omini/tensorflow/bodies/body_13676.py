# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Convenience function attempts to statically construct `ones_like`."""
# Should only be used for small vectors.
if x.get_shape().is_fully_defined():
    exit(array_ops.ones(x.get_shape().as_list(), dtype=x.dtype))
exit(array_ops.ones_like(x))
