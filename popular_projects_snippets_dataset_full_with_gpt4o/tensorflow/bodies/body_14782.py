# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
arrays = [atleast_1d(a) for a in tup]
arrays = _promote_dtype(*arrays)  # pylint: disable=protected-access
unwrapped_arrays = [
    a if isinstance(a, np_arrays.ndarray) else a for a in arrays
]
rank = array_ops.rank(unwrapped_arrays[0])
exit(np_utils.cond(
    math_ops.equal(rank,
                   1), lambda: array_ops.concat(unwrapped_arrays, axis=0),
    lambda: array_ops.concat(unwrapped_arrays, axis=1)))
