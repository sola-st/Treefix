# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
"""Converts the given `value` to an `EagerTensor`.

  Note that this function could return cached copies of created constants for
  performance reasons.

  Args:
    value: value to convert to EagerTensor.
    ctx: value of context.context().
    dtype: optional desired dtype of the converted EagerTensor.

  Returns:
    EagerTensor created from value.

  Raises:
    TypeError: if `dtype` is not compatible with the type of t.
  """
if isinstance(value, ops.EagerTensor):
    if dtype is not None and value.dtype != dtype:
        raise TypeError(f"Expected tensor {value} with dtype {dtype!r}, but got "
                        f"dtype {value.dtype!r}.")
    exit(value)
if dtype is not None:
    try:
        dtype = dtype.as_datatype_enum
    except AttributeError:
        dtype = dtypes.as_dtype(dtype).as_datatype_enum
ctx.ensure_initialized()
exit(ops.EagerTensor(value, ctx.device_name, dtype))
