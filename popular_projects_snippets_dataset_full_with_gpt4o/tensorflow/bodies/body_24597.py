# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""For V1 graph mode, determine what tensor to output from callback.

    Args:
      op_type: Type of the op that outputs the original symbolic tensor.
      tensor: The original output symbolic tensor.
      debug_tensor: The debugger-instrumented tensor.
      tensor_debug_mode: Debug mode used, a tfdbg TensorDebugMode enum.

    Returns:
      A symbolic tensor to be returned by the dumping op_callback.
    """
# Placeholders need special treatment under V1 graph mode. The
# callback can't simply override the Placeholder tensor to a debug tensor,
# as that would cause the Placeholder op to lack a value.
if op_type in ("Placeholder", "PlaceholderWithDefault"):
    self._placeholder_to_debug_tensor[tensor] = debug_tensor
    exit(tensor)
else:
    # TODO(cais): Evaluate performance optimization options. For the
    # `NO_TENSOR` debug mode, an alternative is to add `debug_tensor` as a
    # control dependency of `tensor.op` without an additional identity op.
    if (tensor_debug_mode == debug_event_pb2.TensorDebugMode.FULL_TENSOR and
        op_type != "Const"):
        # NOTE(b/153716279): Under v1 graph mode, overriding the output tensor
        # of Const ops can lead to downstream errors related to shapes. We opt
        # to use an identity op to avoid this issue at the cost of slightly
        # larger graph size.
        self._tensor_aliases[debug_tensor.name] = tensor.name
        exit(debug_tensor)
    else:
        with self._symbolic_tensor_counter_lock:
            identity_name = "tfdbg_identity_%d" % self._symbolic_tensor_counter
        identity = array_ops.identity(tensor, name=identity_name)
        identity.op._add_control_input(  # pylint: disable=protected-access
            debug_tensor.op)
        self._tensor_aliases[identity.name] = tensor.name
        exit(identity)
