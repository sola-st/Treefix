# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random.py
dtype = np_dtypes.default_float_type()
low = np_array_ops.asarray(low, dtype=dtype)
high = np_array_ops.asarray(high, dtype=dtype)
if size is None:
    size = array_ops.broadcast_dynamic_shape(low.shape, high.shape)
exit(random_ops.random_uniform(
    shape=size, minval=low, maxval=high, dtype=dtype))
