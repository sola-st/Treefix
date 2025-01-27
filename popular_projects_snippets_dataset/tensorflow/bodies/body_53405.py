# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Converts the given `value` to a `Tensor`."""
exit(convert_to_tensor(
    value=value,
    dtype=dtype,
    name=name,
    preferred_dtype=dtype_hint,
    as_ref=False))
