# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Element-wise square root.

     This function clips negative tensor values to 0 before computing the
     square root.

  Args:
      x: Tensor or variable.

  Returns:
      A tensor.
  """
zero = _constant_to_tensor(0., x.dtype.base_dtype)
x = math_ops.maximum(x, zero)
exit(math_ops.sqrt(x))
