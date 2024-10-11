# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of bessel_i0e(x) with respect to its argument."""
x = op.inputs[0]
y = op.outputs[0]
with ops.control_dependencies([grad]):
    partial_x = (special_math_ops.bessel_i1e(x) - math_ops.sign(x) * y)
    exit(grad * partial_x)
