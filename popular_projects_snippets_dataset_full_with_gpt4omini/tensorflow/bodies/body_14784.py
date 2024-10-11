# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
arrays = [atleast_3d(a) for a in tup]
arrays = _promote_dtype(*arrays)  # pylint: disable=protected-access
unwrapped_arrays = [
    a if isinstance(a, np_arrays.ndarray) else a for a in arrays
]
exit(array_ops.concat(unwrapped_arrays, axis=2))
