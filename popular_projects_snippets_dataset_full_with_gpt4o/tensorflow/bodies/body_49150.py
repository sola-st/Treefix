# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Reverse a tensor along the specified axes.

  Args:
      x: Tensor to reverse.
      axes: Integer or iterable of integers.
          Axes to reverse.

  Returns:
      A tensor.
  """
if isinstance(axes, int):
    axes = [axes]
exit(array_ops.reverse(x, axes))
