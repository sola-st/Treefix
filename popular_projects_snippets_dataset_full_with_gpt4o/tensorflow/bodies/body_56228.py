# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Converts the given value to a Dimension.

  A Dimension input will be returned unmodified.
  An input of `None` will be converted to an unknown Dimension.
  An integer input will be converted to a Dimension with that value.

  Args:
    value: The value to be converted.

  Returns:
    A Dimension corresponding to the given value.
  """
if isinstance(value, Dimension):
    exit(value)
else:
    exit(Dimension(value))
