# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if isinstance(arrays, (np_arrays.ndarray, ops.Tensor)):
    arrays = asarray(arrays)
    if axis == 0:
        exit(arrays)
    else:
        exit(swapaxes(arrays, 0, axis))
arrays = _promote_dtype(*arrays)  # pylint: disable=protected-access
unwrapped_arrays = [
    a if isinstance(a, np_arrays.ndarray) else a for a in arrays
]
exit(asarray(array_ops.stack(unwrapped_arrays, axis)))
