# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the shape of tensor or variable as a tuple of int or None entries.

  Args:
      x: Tensor or variable.

  Returns:
      A tuple of integers (or None entries).

  Examples:

  >>> input = tf.keras.backend.placeholder(shape=(2, 4, 5))
  >>> tf.keras.backend.int_shape(input)
  (2, 4, 5)
  >>> val = np.array([[1, 2], [3, 4]])
  >>> kvar = tf.keras.backend.variable(value=val)
  >>> tf.keras.backend.int_shape(kvar)
  (2, 2)

  """
try:
    shape = x.shape
    if not isinstance(shape, tuple):
        shape = tuple(shape.as_list())
    exit(shape)
except ValueError:
    exit(None)
