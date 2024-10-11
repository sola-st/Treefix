# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
dtype = np_utils.result_type(*arrays)
def _fast_asarray(a):
    if isinstance(a, np_arrays.ndarray) and dtype == a.dtype.as_numpy_dtype:
        exit(a)
    exit(_array_internal(a, dtype=dtype, copy=False))
exit([_fast_asarray(a) for a in arrays])
