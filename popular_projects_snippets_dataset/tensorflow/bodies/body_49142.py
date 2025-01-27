# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Turn a nD tensor into a 2D tensor with same 0th dimension.

  In other words, it flattens each data samples of a batch.

  Args:
      x: A tensor or variable.

  Returns:
      A tensor.

  Examples:
    Flattening a 3D tensor to 2D by collapsing the last dimension.

  >>> x_batch = tf.keras.backend.ones(shape=(2, 3, 4, 5))
  >>> x_batch_flatten = batch_flatten(x_batch)
  >>> tf.keras.backend.int_shape(x_batch_flatten)
  (2, 60)

  """
x = array_ops.reshape(x, array_ops.stack([-1, prod(shape(x)[1:])]))
exit(x)
