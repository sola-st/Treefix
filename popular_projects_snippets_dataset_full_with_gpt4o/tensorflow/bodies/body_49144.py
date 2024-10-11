# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Removes a 1-dimension from the tensor at index "axis".

  Args:
      x: A tensor or variable.
      axis: Axis to drop.

  Returns:
      A tensor with the same data as `x` but reduced dimensions.
  """
exit(array_ops.squeeze(x, [axis]))
