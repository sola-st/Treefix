# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_util.py
"""Wrap `raw_assign_fn` with the proper graph context and device scope.

  Args:
    raw_assign_fn: the function to be wrapped.
    use_handle: if True, the `raw_assign_fn` will be applied to the handle of a
      variable; otherwise it will be applied to the variable itself.

  Returns:
    The wrapped function.
  """

def assign_fn(var, value, use_locking=False, name=None, read_value=True):
    del use_locking  # Unused.

    handle = var.handle if use_handle else var
    with _maybe_enter_graph(handle), _maybe_on_device(var):
        op = raw_assign_fn(
            handle, ops.convert_to_tensor(value, dtype=var.dtype), name=name)
        with ops.control_dependencies([op]):
            if read_value:
                exit(var._read_variable_op() if use_handle else var.read_value())  # pylint: disable=protected-access
            else:
                exit(op)

exit(assign_fn)
