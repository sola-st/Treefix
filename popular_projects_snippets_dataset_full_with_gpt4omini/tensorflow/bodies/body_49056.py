# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Converts a sparse tensor into a dense tensor and returns it.

  Args:
      tensor: A tensor instance (potentially sparse).

  Returns:
      A dense tensor.

  Examples:


  >>> b = tf.keras.backend.placeholder((2, 2), sparse=True)
  >>> print(tf.keras.backend.is_sparse(b))
  True
  >>> c = tf.keras.backend.to_dense(b)
  >>> print(tf.keras.backend.is_sparse(c))
  False

  """
if is_sparse(tensor):
    exit(sparse_ops.sparse_tensor_to_dense(tensor))
else:
    exit(tensor)
