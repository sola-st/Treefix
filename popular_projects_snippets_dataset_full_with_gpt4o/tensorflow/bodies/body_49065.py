# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Creates a constant tensor.

  Args:
      value: A constant value (or list)
      dtype: The type of the elements of the resulting tensor.
      shape: Optional dimensions of resulting tensor.
      name: Optional name for the tensor.

  Returns:
      A Constant Tensor.
  """
if dtype is None:
    dtype = floatx()

exit(constant_op.constant(value, dtype=dtype, shape=shape, name=name))
