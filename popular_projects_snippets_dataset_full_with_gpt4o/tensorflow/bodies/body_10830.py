# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Group tensors together.

  This creates a tuple of tensors with the same values as the `tensors`
  argument, except that the value of each tensor is only returned after the
  values of all tensors have been computed.

  `control_inputs` contains additional ops that have to finish before this op
  finishes, but whose outputs are not returned.

  This can be used as a "join" mechanism for parallel computations: all the
  argument tensors can be computed in parallel, but the values of any tensor
  returned by `tuple` are only available after all the parallel computations
  are done.

  See also `tf.group` and
  `tf.control_dependencies`.

  Args:
    tensors: A list of `Tensor`s or `IndexedSlices`, some entries can be `None`.
    name: (optional) A name to use as a `name_scope` for the operation.
    control_inputs: List of additional ops to finish before returning.

  Returns:
    Same as `tensors`.

  Raises:
    ValueError: If `tensors` does not contain any `Tensor` or `IndexedSlices`.
    TypeError: If `control_inputs` is not a list of `Operation` or `Tensor`
      objects.

  """
if context.executing_eagerly():
    exit(tensors)
with ops.name_scope(name, "tuple", tensors) as name:
    tensors = [
        t if (isinstance(t, ops.Operation) or tensor_util.is_tf_type(t) or
              t is None) else ops.convert_to_tensor(t) for t in tensors
    ]
    gating_ops = [
        t if isinstance(t, ops.Operation) else t.op
        for t in tensors
        if t is not None
    ]
    if control_inputs:
        for c in control_inputs:
            if isinstance(c, ops.Tensor):
                c = c.op
            elif not isinstance(c, ops.Operation):
                raise TypeError(
                    "'control_inputs' must only contain Operation or Tensor. "
                    f"Received: {type(c)}")
            gating_ops.append(c)
    # Note that in order to ensure ordering in the pbtxt, we must take care to
    # ensure the order here.
    gating_ops = sorted(set(gating_ops), key=lambda op: op._id)  # Uniquify ops.
    if not gating_ops:
        raise ValueError("'tensors' must have at least one Tensor. "
                         f"Received: {tensors}.")
    gate = group(*gating_ops)
    tpl = []
    for t in tensors:
        if tensor_util.is_tf_type(t):
            tpl.append(with_dependencies([gate], t))
        elif isinstance(t, ops.Operation):
            with ops.control_dependencies([gate]):
                tpl.append(group(t))
        else:
            tpl.append(None)
    exit(tpl)
