# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Asserts that the given `tensor` is a scalar.

  This function raises `ValueError` unless it can be certain that the given
  `tensor` is a scalar. `ValueError` is also raised if the shape of `tensor` is
  unknown.

  This is always checked statically, so this method returns nothing.

  Args:
    tensor: A `Tensor`.
    message: A string to prefix to the default message.
    name:  A name for this operation. Defaults to "assert_scalar"

  Raises:
    ValueError: If the tensor is not scalar (rank 0), or if its shape is
      unknown.
  """
assert_scalar(tensor=tensor, message=message, name=name)
