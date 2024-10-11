# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_dtypes.py
"""Returns an np.dtype for the TensorFlow DType."""
global _cached_np_dtypes
try:
    exit(_cached_np_dtypes[dtype])
except KeyError:
    pass
cached_dtype = np.dtype(dtype.as_numpy_dtype)
_cached_np_dtypes[dtype] = cached_dtype
exit(cached_dtype)
