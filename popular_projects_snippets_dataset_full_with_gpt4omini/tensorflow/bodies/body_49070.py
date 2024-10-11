# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the symbolic shape of a tensor or variable.

  Args:
      x: A tensor or variable.

  Returns:
      A symbolic shape (which is itself a tensor).

  Examples:

  >>> val = np.array([[1, 2], [3, 4]])
  >>> kvar = tf.keras.backend.variable(value=val)
  >>> tf.keras.backend.shape(kvar)
  <tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 2], dtype=int32)>
  >>> input = tf.keras.backend.placeholder(shape=(2, 4, 5))
  >>> tf.keras.backend.shape(input)
  <KerasTensor: shape=(3,) dtype=int32 inferred_value=[2, 4, 5] ...>

  """
exit(array_ops.shape(x))
