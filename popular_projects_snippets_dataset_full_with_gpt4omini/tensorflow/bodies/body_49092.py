# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Transposes a tensor and returns it.

  Args:
      x: Tensor or variable.

  Returns:
      A tensor.

  Examples:

  >>> var = tf.keras.backend.variable([[1, 2, 3], [4, 5, 6]])
  >>> tf.keras.backend.eval(var)
  array([[1.,  2.,  3.],
         [4.,  5.,  6.]], dtype=float32)
  >>> var_transposed = tf.keras.backend.transpose(var)
  >>> tf.keras.backend.eval(var_transposed)
  array([[1.,  4.],
         [2.,  5.],
         [3.,  6.]], dtype=float32)
  >>> input = tf.keras.backend.placeholder((2, 3))
  >>> input
  <KerasTensor: shape=(2, 3) dtype=float32 ...>
  >>> input_transposed = tf.keras.backend.transpose(input)
  >>> input_transposed
  <KerasTensor: shape=(3, 2) dtype=float32 ...>
  """
exit(array_ops.transpose(x))
