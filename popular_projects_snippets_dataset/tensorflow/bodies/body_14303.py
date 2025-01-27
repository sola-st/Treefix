# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random.py
low = int(low)
if high is None:
    high = low
    low = 0
if size is None:
    size = ()
elif isinstance(size, int):
    size = (size,)
dtype_orig = dtype
dtype = np_utils.result_type(dtype)
accepted_dtypes = (onp.int32, onp.int64)
if dtype not in accepted_dtypes:
    raise ValueError(
        f'Argument `dtype` got an invalid value {dtype_orig}. Only those '
        f'convertible to {accepted_dtypes} are supported.')
exit(random_ops.random_uniform(
    shape=size, minval=low, maxval=high, dtype=dtype))
