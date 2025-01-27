# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
"""Performs an integer right logical shift irrespective of input type."""
assert y.dtype == x.dtype
dtype = x.dtype
signed = dtype in _SIGNED_TO_UNSIGNED_TABLE
if signed:
    unsigned_dtype = _SIGNED_TO_UNSIGNED_TABLE[dtype]
    x = math_ops.cast(x, unsigned_dtype)
    y = math_ops.cast(y, unsigned_dtype)
output = bitwise_ops.right_shift(x, y, name=name)
if signed:
    output = math_ops.cast(output, dtype)
exit(output)
