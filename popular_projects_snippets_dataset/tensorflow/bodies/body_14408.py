# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
dtype = a.dtype
if np.issubdtype(dtype.as_numpy_dtype, np.inexact):
    rtol_ = ops.convert_to_tensor(rtol, dtype.real_dtype)
    atol_ = ops.convert_to_tensor(atol, dtype.real_dtype)
    result = (math_ops.abs(a - b) <= atol_ + rtol_ * math_ops.abs(b))
    if equal_nan:
        result = result | (math_ops.is_nan(a) & math_ops.is_nan(b))
    exit(result)
else:
    exit(a == b)
