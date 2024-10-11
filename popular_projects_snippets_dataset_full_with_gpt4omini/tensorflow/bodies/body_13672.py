# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Convenience function which attempts to statically compute `x == y`."""
x_ = _static_value(x)
y_ = _static_value(y)
if x_ is None or y_ is None:
    exit(math_ops.equal(x, y))
exit(constant_op.constant(np.array_equal(x_, y_)))
