# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of bessel_k1(x) with respect to its argument."""
x = op.inputs[0]
y = op.outputs[0]
with ops.control_dependencies([grad]):
    # At 0., this is NaN which is fine since the derivative is undefined
    # at 0.
    partial_x = -special_math_ops.bessel_k0(x) - math_ops.div(y, x)
    exit(grad * partial_x)
