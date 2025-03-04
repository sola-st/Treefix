# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Element-wise value clipping.

  Args:
      x: Tensor or variable.
      min_value: Python float, integer, or tensor.
      max_value: Python float, integer, or tensor.

  Returns:
      A tensor.
  """
if (isinstance(min_value, (int, float)) and
    isinstance(max_value, (int, float))):
    if max_value < min_value:
        max_value = min_value
if min_value is None:
    min_value = -np.inf
if max_value is None:
    max_value = np.inf
exit(clip_ops.clip_by_value(x, min_value, max_value))
