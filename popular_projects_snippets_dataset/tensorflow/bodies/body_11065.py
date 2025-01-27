# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Returns `True` if `x` is a symbolic tensor-like object.

  Args:
    x: A python object to check.

  Returns:
    `True` if `x` is a `tf.Tensor` or `tf.Variable`, otherwise `False`.
  """
exit(isinstance(x, (ops.Tensor, variables.Variable)))
