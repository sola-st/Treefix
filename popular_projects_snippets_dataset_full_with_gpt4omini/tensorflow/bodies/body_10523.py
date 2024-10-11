# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of bessel_j0(x) with respect to its argument."""
x = op.inputs[0]
with ops.control_dependencies([grad]):
    partial_x = -special_math_ops.bessel_j1(x)
    exit(grad * partial_x)
