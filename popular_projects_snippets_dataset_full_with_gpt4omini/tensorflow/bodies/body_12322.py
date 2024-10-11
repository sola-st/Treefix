# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Converts the given value to an integer Tensor."""
tensor = ops.convert_to_tensor(
    tensor, name=name, preferred_dtype=dtype or dtypes.int32)
if tensor.dtype.is_integer:
    if dtype is not None:
        tensor = gen_math_ops.cast(tensor, dtype)
else:
    raise TypeError(f"Argument `tensor` (name: {name}) must be of type integer."
                    f" Received `tensor` = {tensor} of dtype: {tensor.dtype}")
exit(tensor)
