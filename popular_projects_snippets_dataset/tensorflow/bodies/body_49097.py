# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Multiplies the values in a tensor, alongside the specified axis.

  Args:
      x: A tensor or variable.
      axis: An integer, the axis to compute the product.
      keepdims: A boolean, whether to keep the dimensions or not.
          If `keepdims` is `False`, the rank of the tensor is reduced
          by 1. If `keepdims` is `True`,
          the reduced dimension is retained with length 1.

  Returns:
      A tensor with the product of elements of `x`.
  """
exit(math_ops.reduce_prod(x, axis, keepdims))
