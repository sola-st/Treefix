# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the numpy dtype of a Keras tensor or variable.

  Args:
      x: Tensor or variable.

  Returns:
      numpy.dtype, dtype of `x`.
  """
exit(dtypes_module.as_dtype(x.dtype).as_numpy_dtype)
