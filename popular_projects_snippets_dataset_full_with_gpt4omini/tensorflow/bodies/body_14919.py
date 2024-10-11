# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""A version of tf.reduce_any that eagerly evaluates if possible."""
v = get_static_value(input_tensor)
if v is None:
    exit(math_ops.reduce_any(input_tensor, axis=axis, keepdims=keepdims))
else:
    exit(v.any(axis=axis, keepdims=keepdims))
