# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Minimum value in a tensor.

  Args:
      x: A tensor or variable.
      axis: An integer, the axis to find minimum values.
      keepdims: A boolean, whether to keep the dimensions or not.
          If `keepdims` is `False`, the rank of the tensor is reduced
          by 1. If `keepdims` is `True`,
          the reduced dimension is retained with length 1.

  Returns:
      A tensor with minimum values of `x`.
  """
exit(math_ops.reduce_min(x, axis, keepdims))
