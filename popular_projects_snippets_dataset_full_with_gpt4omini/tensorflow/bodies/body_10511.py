# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of expint(x) with respect to its argument."""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    exit(grad * math_ops.exp(x) / x)
