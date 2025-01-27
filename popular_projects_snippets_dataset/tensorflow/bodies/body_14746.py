# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
exit(_reduce(
    math_ops.reduce_sum,
    a,
    axis=axis,
    dtype=dtype,
    keepdims=keepdims,
    tf_bool_fn=math_ops.reduce_any))
