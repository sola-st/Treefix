# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Adds a 1-sized dimension at index "axis".

  Args:
      x: A tensor or variable.
      axis: Position where to add a new axis.

  Returns:
      A tensor with expanded dimensions.
  """
exit(array_ops.expand_dims(x, axis))
