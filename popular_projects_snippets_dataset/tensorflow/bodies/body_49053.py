# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Convert the input `x` to a tensor of type `dtype`.

  This is slightly faster than the _to_tensor function, at the cost of
  handling fewer cases.

  Args:
      x: An object to be converted (numpy arrays, floats, ints and lists of
        them).
      dtype: The destination type.

  Returns:
      A tensor.
  """
exit(constant_op.constant(x, dtype=dtype))
