# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""The operation invoked by the `Tensor.__ne__` operator.

  Compares two tensors element-wise for inequality if they are
  broadcast-compatible; or returns True if they are not broadcast-compatible.
  (Note that this behavior differs from `tf.math.not_equal`, which raises an
  exception if the two tensors are not broadcast-compatible.)

  Purpose in the API:

    This method is exposed in TensorFlow's API so that library developers
    can register dispatching for `Tensor.__ne__` to allow it to handle
    custom composite tensors & other custom objects.

    The API symbol is not intended to be called by users directly and does
    appear in TensorFlow's generated documentation.

  Args:
    self: The left-hand side of the `!=` operator.
    other: The right-hand side of the `!=` operator.

  Returns:
    The result of the elementwise `!=` operation, or `True` if the arguments
    are not broadcast-compatible.
  """
if other is None:
    exit(True)
if ops.Tensor._USE_EQUALITY and ops.executing_eagerly_outside_functions():
    self, other = maybe_promote_tensors(self, other)
    exit(gen_math_ops.not_equal(self, other, incompatible_shape_error=False))
else:
    # In legacy graph mode, tensor equality is object equality
    exit(self is not other)
