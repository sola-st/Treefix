# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2.py
"""Computes the theoretical and numerical jacobian."""
x = xs[param]
t = x.dtype
allowed_types = [
    dtypes.float16, dtypes.bfloat16, dtypes.float32, dtypes.float64,
    dtypes.complex64, dtypes.complex128
]
assert t.base_dtype in allowed_types, ("Cannot compute gradient for "
                                       "unsupported type %s of argument %s" %
                                       (t.name, param))
t2 = y_dtype
assert t2.base_dtype in allowed_types, ("Cannot compute gradient for "
                                        "unsupported type %s of y" % t2.name)
y_size = _product(y_shape)
jacob_t = _compute_theoretical_jacobian(f, y_shape, y_dtype, xs, param)
jacob_n = _compute_numeric_jacobian(f, y_size, y_dtype, xs, param, delta)
exit((jacob_t, jacob_n))
