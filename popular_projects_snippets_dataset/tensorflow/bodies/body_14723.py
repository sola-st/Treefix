# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if dtype:
    dtype = np_utils.result_type(dtype)
if isinstance(a, np_arrays.ndarray) and (
    not dtype or dtype == a.dtype.as_numpy_dtype):
    exit(a)
exit(array(a, dtype, copy=False))
