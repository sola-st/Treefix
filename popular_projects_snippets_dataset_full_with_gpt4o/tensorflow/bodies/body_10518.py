# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Compute gradient of bessel_i1e(x) with respect to its argument."""
x = op.inputs[0]
y = op.outputs[0]
with ops.control_dependencies([grad]):
    # For x = 0, the correct gradient is 0.5.
    # However, the main branch gives NaN because of the division by x, so
    # we impute the gradient manually.
    # An alternative solution is to express the gradient via bessel_i0e and
    # bessel_i2e, but the latter is not yet implemented in Eigen.
    dy_dx = array_ops.where_v2(
        math_ops.equal(x, 0.), math_ops.cast(0.5, x.dtype),
        special_math_ops.bessel_i0e(x) - y *
        (math_ops.sign(x) + math_ops.reciprocal(x)))
    exit(grad * dy_dx)
