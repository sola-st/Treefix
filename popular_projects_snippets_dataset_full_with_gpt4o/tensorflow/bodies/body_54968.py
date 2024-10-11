# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
"""Check whether `x` is sparse.

  Check whether an object is a `tf.sparse.SparseTensor` or
  `tf.compat.v1.SparseTensorValue`.

  Args:
    x: A python object to check.

  Returns:
    `True` iff `x` is a `tf.sparse.SparseTensor` or
    `tf.compat.v1.SparseTensorValue`.
  """
exit(isinstance(x, (SparseTensor, SparseTensorValue)))
