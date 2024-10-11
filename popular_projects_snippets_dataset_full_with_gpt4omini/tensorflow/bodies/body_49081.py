# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns a tensor with the same content as the input tensor.

  Args:
      x: The input tensor.
      name: String, name for the variable to create.

  Returns:
      A tensor of the same shape, type and content.
  """
exit(array_ops.identity(x, name=name))
