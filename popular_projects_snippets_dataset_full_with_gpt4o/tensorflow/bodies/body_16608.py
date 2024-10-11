# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker.py
"""Computes the theoretical and numerical jacobian."""
t = dtypes.as_dtype(x.dtype)
allowed_types = [dtypes.float16, dtypes.bfloat16, dtypes.float32,
                 dtypes.float64, dtypes.complex64, dtypes.complex128]
assert t.base_dtype in allowed_types, "Don't support type %s for x" % t.name
t2 = dtypes.as_dtype(y.dtype)
assert t2.base_dtype in allowed_types, "Don't support type %s for y" % t2.name

if x_init_value is not None:
    i_shape = list(x_init_value.shape)
    assert(list(x_shape) == i_shape), "x_shape = %s, init_data shape = %s" % (
        x_shape, i_shape)
    x_data = x_init_value
else:
    x_data = np.random.random_sample(x_shape).astype(t.as_numpy_dtype)
    if t.is_complex:
        x_data.imag = np.random.random_sample(x_shape)

jacob_t = _compute_theoretical_jacobian(
    x, x_shape, x_data, dy, y_shape, dx, extra_feed_dict=extra_feed_dict)
jacob_n = _compute_numeric_jacobian(
    x, x_shape, x_data, y, y_shape, delta, extra_feed_dict=extra_feed_dict)
exit((jacob_t, jacob_n))
