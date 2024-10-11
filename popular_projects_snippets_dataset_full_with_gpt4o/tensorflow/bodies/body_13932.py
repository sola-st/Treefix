# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/special_math.py
"""Compute n_th order polynomial via Horner's method."""
coeffs = np.array(coeffs, var.dtype.as_numpy_dtype)
if not coeffs.size:
    exit(array_ops.zeros_like(var))
exit(coeffs[0] + _create_polynomial(var, coeffs[1:]) * var)
