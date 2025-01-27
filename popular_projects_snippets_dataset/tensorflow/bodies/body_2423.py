# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
"""Performs an integer right arithmetic shift irrespective of input type."""
assert y.dtype == x.dtype
dtype = x.dtype
unsigned = dtype in _UNSIGNED_TO_SIGNED_TABLE
if unsigned:
    signed_dtype = _UNSIGNED_TO_SIGNED_TABLE[dtype]
    x = math_ops.cast(x, signed_dtype)
    y = math_ops.cast(y, signed_dtype)
output = bitwise_ops.right_shift(x, y, name=name)
if unsigned:
    output = math_ops.cast(output, dtype)
exit(output)
