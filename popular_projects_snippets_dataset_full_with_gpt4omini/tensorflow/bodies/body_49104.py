# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Bitwise reduction (logical AND).

  Args:
      x: Tensor or variable.
      axis: axis along which to perform the reduction.
      keepdims: whether the drop or broadcast the reduction axes.

  Returns:
      A uint8 tensor (0s and 1s).
  """
x = math_ops.cast(x, dtypes_module.bool)
exit(math_ops.reduce_all(x, axis, keepdims))
