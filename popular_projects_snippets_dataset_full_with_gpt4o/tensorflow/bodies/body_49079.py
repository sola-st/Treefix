# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Instantiates an all-zeros variable of the same shape as another tensor.

  Args:
      x: Keras variable or Keras tensor.
      dtype: dtype of returned Keras variable.
             `None` uses the dtype of `x`.
      name: name for the variable to create.

  Returns:
      A Keras variable with the shape of `x` filled with zeros.

  Example:

  ```python
  from tensorflow.keras import backend as K
  kvar = K.variable(np.random.random((2,3)))
  kvar_zeros = K.zeros_like(kvar)
  K.eval(kvar_zeros)
  # array([[ 0.,  0.,  0.], [ 0.,  0.,  0.]], dtype=float32)
  ```
  """
exit(array_ops.zeros_like(x, dtype=dtype, name=name))
