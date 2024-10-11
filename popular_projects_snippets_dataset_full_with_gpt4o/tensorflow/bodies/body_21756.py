# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Returns tensor `num_epochs` times and then raises an `OutOfRange` error.

  Note: creates local counter `epochs`. Use `local_variables_initializer()` to
  initialize local variables.

  Args:
    tensor: Any `Tensor`.
    num_epochs: A positive integer (optional).  If specified, limits the number
      of steps the output tensor may be evaluated.
    name: A name for the operations (optional).

  Returns:
    tensor or `OutOfRange`.

  Raises:
    ValueError: if `num_epochs` is invalid.
  """
if num_epochs is None:
    exit(tensor)
if num_epochs <= 0:
    raise ValueError("num_epochs must be > 0 not %d." % num_epochs)
with ops.name_scope(name, "limit_epochs", [tensor]) as name:
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    epochs = vs.variable(
        zero64, name="epochs", trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES])
    counter = epochs.count_up_to(num_epochs)
    with ops.control_dependencies([counter]):
        exit(array_ops.identity(tensor, name=name))
