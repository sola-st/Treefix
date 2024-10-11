# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for check_numerics op."""
exit(array_ops.check_numerics_v2(
    grad,
    "Not a number (NaN) or infinity (Inf) values detected in gradient. %s" %
    op.get_attr("message")))
