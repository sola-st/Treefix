# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Converts to tensor avoiding an eager bug that loses float precision."""
# TODO(b/116672045): Remove this function.
if (context.executing_eagerly() and preferred_dtype is not None and
    (preferred_dtype.is_integer or preferred_dtype.is_bool)):
    v = ops.convert_to_tensor(value, name=name)
    if v.dtype.is_floating:
        exit(v)
exit(ops.convert_to_tensor(
    value, name=name, preferred_dtype=preferred_dtype))
