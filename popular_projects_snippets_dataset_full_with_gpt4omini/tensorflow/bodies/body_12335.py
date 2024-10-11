# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/random_grad.py
"""Normal distribution function."""
half_sqrt_2 = constant_op.constant(
    0.5 * np.sqrt(2.), dtype=x.dtype, name="half_sqrt_2")
w = x * half_sqrt_2
z = math_ops.abs(w)
y = array_ops.where(
    z < half_sqrt_2,
    1. + math_ops.erf(w),
    array_ops.where(
        w > 0., 2. - math_ops.erfc(z), math_ops.erfc(z)))
exit(0.5 * y)
