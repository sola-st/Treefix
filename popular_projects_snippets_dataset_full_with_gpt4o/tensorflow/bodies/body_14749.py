# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if out is not None:
    raise ValueError('Setting out is not supported.')
exit(_reduce(
    math_ops.reduce_max,
    a,
    axis=axis,
    dtype=None,
    keepdims=keepdims,
    promote_int=None,
    tf_bool_fn=math_ops.reduce_any,
    preserve_bool=True))
