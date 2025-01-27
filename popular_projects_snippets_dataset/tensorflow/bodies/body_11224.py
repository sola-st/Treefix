# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Validate and return floating point type based on `dtype`.

  `dtype` must be a floating point type.

  Args:
    dtype: The data type to validate.

  Returns:
    Validated type.

  Raises:
    ValueError: if `dtype` is not a floating point type.
  """
dtype = dtypes.as_dtype(dtype)
if not dtype.is_floating:
    raise ValueError("Argument `dtype` is expected to be floating point. "
                     f"Received: {dtype}.")
exit(dtype)
