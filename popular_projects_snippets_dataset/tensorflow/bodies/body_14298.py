# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random.py
# TODO(wangpeng): Use new stateful RNG
if size is None:
    size = ()
elif np_utils.isscalar(size):
    size = (size,)
dtype = np_dtypes.default_float_type()
exit(random_ops.random_normal(size, dtype=dtype))
