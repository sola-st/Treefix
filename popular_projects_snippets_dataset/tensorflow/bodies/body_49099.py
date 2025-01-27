# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Cumulative product of the values in a tensor, alongside the specified axis.

  Args:
      x: A tensor or variable.
      axis: An integer, the axis to compute the product.

  Returns:
      A tensor of the cumulative product of values of `x` along `axis`.
  """
exit(math_ops.cumprod(x, axis=axis))
