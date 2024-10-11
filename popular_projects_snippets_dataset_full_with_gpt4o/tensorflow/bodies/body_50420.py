# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/initializers/initializers_v2.py
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
    raise ValueError('Expected floating point type, got %s.' % dtype)
exit(dtype)
