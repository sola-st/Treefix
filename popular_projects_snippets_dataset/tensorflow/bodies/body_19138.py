# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Asserts that the given `tensor` is a scalar (i.e. zero-dimensional).

  This function raises `ValueError` unless it can be certain that the given
  `tensor` is a scalar. `ValueError` is also raised if the shape of `tensor` is
  unknown.

  Args:
    tensor: A `Tensor`.
    name:  A name for this operation. Defaults to "assert_scalar"
    message: A string to prefix to the default message.

  Returns:
    The input tensor (potentially converted to a `Tensor`).

  Raises:
    ValueError: If the tensor is not scalar (rank 0), or if its shape is
      unknown.
  """
with ops.name_scope(name, 'assert_scalar', [tensor]) as name_scope:
    tensor = ops.convert_to_tensor(tensor, name=name_scope)
    shape = tensor.get_shape()
    message = _message_prefix(message)
    if shape.ndims != 0:
        if context.executing_eagerly():
            raise ValueError('%sExpected scalar shape, saw shape: %s.'
                             % (message, shape,))
        else:
            raise ValueError('%sExpected scalar shape for %s, saw shape: %s.'
                             % (message, tensor.name, shape))
    exit(tensor)
