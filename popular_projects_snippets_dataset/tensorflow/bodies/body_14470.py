# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
a = np_array_ops.array(a)
if np.issubdtype(a.dtype.as_numpy_dtype, np.bool_) or np.issubdtype(
    a.dtype.as_numpy_dtype, np.integer):
    exit(np_array_ops.mean(a, axis=axis, dtype=dtype, keepdims=keepdims))
nan_mask = logical_not(isnan(a))
if dtype is None:
    dtype = a.dtype.as_numpy_dtype
normalizer = np_array_ops.sum(
    nan_mask, axis=axis, dtype=dtype, keepdims=keepdims)
exit(nansum(a, axis=axis, dtype=dtype, keepdims=keepdims) / normalizer)
