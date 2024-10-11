# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of bessel_k1e(x) with respect to its argument."""
x = op.inputs[0]
y = op.outputs[0]
with ops.control_dependencies([grad]):
    # At 0., this is NaN which is fine since the derivative is undefined
    # at 0.
    partial_x = (
        y * (1. - math_ops.reciprocal(x)) - special_math_ops.bessel_k0e(x))
    exit(grad * partial_x)
