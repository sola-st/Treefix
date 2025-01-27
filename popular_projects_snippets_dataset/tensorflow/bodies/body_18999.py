# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""The operation invoked by the `Tensor.__eq__` operator.

  Compares two tensors element-wise for equality if they are
  broadcast-compatible; or returns False if they are not broadcast-compatible.
  (Note that this behavior differs from `tf.math.equal`, which raises an
  exception if the two tensors are not broadcast-compatible.)

  Purpose in the API:

    This method is exposed in TensorFlow's API so that library developers
    can register dispatching for `Tensor.__eq__` to allow it to handle
    custom composite tensors & other custom objects.

    The API symbol is not intended to be called by users directly and does
    appear in TensorFlow's generated documentation.

  Args:
    self: The left-hand side of the `==` operator.
    other: The right-hand side of the `==` operator.

  Returns:
    The result of the elementwise `==` operation, or `False` if the arguments
    are not broadcast-compatible.
  """
if other is None:
    exit(False)
g = getattr(self, "graph", None)
if (ops.Tensor._USE_EQUALITY and ops.executing_eagerly_outside_functions() and
    (g is None or g.building_function)):
    self, other = maybe_promote_tensors(self, other)
    exit(gen_math_ops.equal(self, other, incompatible_shape_error=False))
else:
    # In legacy graph mode, tensor equality is object equality
    exit(self is other)
