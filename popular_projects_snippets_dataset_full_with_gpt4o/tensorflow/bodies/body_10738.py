# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Check if the shapes of the loops variables are invariants.

  Args:
    merge_var: The tensor representing the initial values of the loop
      variables.
    next_var: The tensor representing the values of the loop variables
      after one loop iteration.

  Raises:
    ValueError: If any tensor in `merge_var` has a more specific shape than
      its corresponding tensor in `next_var`.
  """
if isinstance(merge_var, ops.Tensor):
    m_shape = merge_var.get_shape()
    n_shape = next_var.get_shape()
    if not _ShapeLessThanOrEqual(n_shape, m_shape):
        enter = merge_var.op.inputs[0].op
        assert util.IsLoopEnter(enter)
        input_t = enter.inputs[0]
        raise ValueError(
            "Input tensor '%s' enters the loop with shape %s, but has shape %s "
            "after one iteration. To allow the shape to vary across iterations, "
            "use the `shape_invariants` argument of tf.while_loop to specify a "
            "less-specific shape." % (input_t.name, input_t.shape, n_shape))
else:
    raise TypeError("'merge_var' must be a Tensor. "
                    f"Received: {type(merge_var)}.")
