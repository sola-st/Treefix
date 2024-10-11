# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if out is not None:
    raise ValueError('Setting out is not supported.')
exit(_reduce(
    math_ops.reduce_mean,
    a,
    axis=axis,
    dtype=dtype,
    keepdims=keepdims,
    promote_int=_TO_FLOAT))
