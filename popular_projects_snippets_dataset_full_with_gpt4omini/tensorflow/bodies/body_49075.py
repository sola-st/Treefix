# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Evaluates the value of a variable.

  Args:
      x: A variable.

  Returns:
      A Numpy array.

  Examples:

  >>> kvar = tf.keras.backend.variable(np.array([[1, 2], [3, 4]]),
  ...                                  dtype='float32')
  >>> tf.keras.backend.eval(kvar)
  array([[1.,  2.],
         [3.,  4.]], dtype=float32)

  """
exit(get_value(to_dense(x)))
