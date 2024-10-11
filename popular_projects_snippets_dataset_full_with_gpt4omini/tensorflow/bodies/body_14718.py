# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if not isinstance(shape, np_arrays.ndarray):
    shape = asarray(np_arrays.convert_to_tensor(shape, dtype_hint=np.int32))
shape = atleast_1d(shape)
fill_value = asarray(fill_value, dtype=dtype)
exit(array_ops.broadcast_to(fill_value, shape))
