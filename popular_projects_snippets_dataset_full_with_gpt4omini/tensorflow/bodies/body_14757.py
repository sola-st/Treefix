# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
a = asarray(a)
dtype = a.dtype.as_numpy_dtype
factor = math.pow(10, decimals)
if np.issubdtype(dtype, np.inexact):
    factor = math_ops.cast(factor, dtype)
else:
    # Use float as the working dtype when a.dtype is exact (e.g. integer),
    # because `decimals` can be negative.
    float_dtype = np_dtypes.default_float_type()
    a = a.astype(float_dtype)
    factor = math_ops.cast(factor, float_dtype)
a = math_ops.multiply(a, factor)
a = math_ops.round(a)
a = math_ops.divide(a, factor)
exit(a.astype(dtype))
