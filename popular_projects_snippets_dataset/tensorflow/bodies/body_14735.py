# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
dtype = np_utils._result_type_binary(t1, t2)  # pylint: disable=protected-access
if not(
    isinstance(t1, np_arrays.ndarray) and dtype == t1.dtype.as_numpy_dtype):
    t1 = _array_internal(t1, dtype=dtype, copy=False)
if not(
    isinstance(t2, np_arrays.ndarray) and dtype == t2.dtype.as_numpy_dtype):
    t2 = _array_internal(t2, dtype=dtype, copy=False)
exit((t1, t2))
