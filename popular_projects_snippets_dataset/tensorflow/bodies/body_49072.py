# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the number of axes in a tensor, as an integer.

  Args:
      x: Tensor or variable.

  Returns:
      Integer (scalar), number of axes.

  Examples:


  >>> input = tf.keras.backend.placeholder(shape=(2, 4, 5))
  >>> val = np.array([[1, 2], [3, 4]])
  >>> kvar = tf.keras.backend.variable(value=val)
  >>> tf.keras.backend.ndim(input)
  3
  >>> tf.keras.backend.ndim(kvar)
  2

  """
exit(x.shape.rank)
