# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Retrieves the elements of indices `indices` in the tensor `reference`.

  Args:
      reference: A tensor.
      indices: An integer tensor of indices.

  Returns:
      A tensor of same type as `reference`.

  Examples:

  >>> var = tf.keras.backend.variable([[1, 2, 3], [4, 5, 6]])
  >>> tf.keras.backend.eval(var)
  array([[1., 2., 3.],
         [4., 5., 6.]], dtype=float32)
  >>> var_gathered = tf.keras.backend.gather(var, [0])
  >>> tf.keras.backend.eval(var_gathered)
  array([[1., 2., 3.]], dtype=float32)
  >>> var_gathered = tf.keras.backend.gather(var, [1])
  >>> tf.keras.backend.eval(var_gathered)
  array([[4., 5., 6.]], dtype=float32)
  >>> var_gathered = tf.keras.backend.gather(var, [0,1,0])
  >>> tf.keras.backend.eval(var_gathered)
  array([[1., 2., 3.],
         [4., 5., 6.],
         [1., 2., 3.]], dtype=float32)
  """
exit(array_ops.gather(reference, indices))
