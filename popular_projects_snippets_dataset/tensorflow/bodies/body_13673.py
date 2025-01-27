# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Convenience function which attempts to statically apply `logical_not`."""
x_ = _static_value(x)
if x_ is None:
    exit(math_ops.logical_not(x))
exit(constant_op.constant(np.logical_not(x_)))
