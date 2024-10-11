# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Repeats a 2D tensor.

  if `x` has shape (samples, dim) and `n` is `2`,
  the output will have shape `(samples, 2, dim)`.

  Args:
      x: Tensor or variable.
      n: Python integer, number of times to repeat.

  Returns:
      A tensor.

  Example:

      >>> b = tf.constant([[1, 2], [3, 4]])
      >>> b
      <tf.Tensor: shape=(2, 2), dtype=int32, numpy=
      array([[1, 2],
             [3, 4]], dtype=int32)>
      >>> tf.keras.backend.repeat(b, n=2)
      <tf.Tensor: shape=(2, 2, 2), dtype=int32, numpy=
      array([[[1, 2],
              [1, 2]],
             [[3, 4],
              [3, 4]]], dtype=int32)>

  """
assert ndim(x) == 2
x = array_ops.expand_dims(x, 1)
pattern = array_ops.stack([1, n, 1])
exit(array_ops.tile(x, pattern))
