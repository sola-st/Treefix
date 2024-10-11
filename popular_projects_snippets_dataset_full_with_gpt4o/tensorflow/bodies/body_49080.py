# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Instantiates an all-ones variable of the same shape as another tensor.

  Args:
      x: Keras variable or tensor.
      dtype: String, dtype of returned Keras variable.
           None uses the dtype of x.
      name: String, name for the variable to create.

  Returns:
      A Keras variable with the shape of x filled with ones.

  Example:

  >>> kvar = tf.keras.backend.variable(np.random.random((2,3)))
  >>> kvar_ones = tf.keras.backend.ones_like(kvar)
  >>> tf.keras.backend.eval(kvar_ones)
  array([[1.,  1.,  1.],
         [1.,  1.,  1.]], dtype=float32)

  """
exit(array_ops.ones_like(x, dtype=dtype, name=name))
