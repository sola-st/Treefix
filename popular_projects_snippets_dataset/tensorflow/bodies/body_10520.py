# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of bessel_k0e(x) with respect to its argument."""
x = op.inputs[0]
y = op.outputs[0]
with ops.control_dependencies([grad]):
    partial_x = (y - special_math_ops.bessel_k1e(x))
    exit(grad * partial_x)
