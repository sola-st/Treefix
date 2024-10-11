# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if isinstance(a, np_arrays.ndarray) and dtype == a.dtype.as_numpy_dtype:
    exit(a)
exit(_array_internal(a, dtype=dtype, copy=False))
