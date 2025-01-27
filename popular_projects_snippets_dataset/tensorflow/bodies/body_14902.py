# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
arrays_and_dtypes = [
    _maybe_get_dtype(x) for x in nest.flatten(arrays_and_dtypes)
]
if not arrays_and_dtypes:
    # If arrays_and_dtypes is an empty list, let numpy decide what the dtype is.
    arrays_and_dtypes = [np.asarray([])]
exit(np_dtypes._result_type(*arrays_and_dtypes))  # pylint: disable=protected-access
