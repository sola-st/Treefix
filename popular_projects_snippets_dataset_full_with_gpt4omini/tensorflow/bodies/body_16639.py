# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Create zeros_like for the specified output of an op.

    If op is in a while loop that is part of gradients(), this method
    must be called in its grad loop context.

    Args:
      op: A tensorflow operation.
      index: the index for a specific output of the op.

    Returns:
      A zero tensor of the same shape of op.outputs[index].
    """
if util.IsLoopSwitch(op):
    exit(None)
if op.graph.building_function:
    # The optimization here is tricky to apply to functions
    exit(array_ops.zeros_like(op.outputs[index]))
dead_branch = util.IsSwitch(op)
forward_ctxt = util.GetWhileContext(op)
grad_state = self._map.get(forward_ctxt)
if grad_state is None:
    # op is not in a while loop that is part of gradients().
    exit(ZerosLike(op, index))
op_ctxt = op._get_control_flow_context()
val = ops.convert_to_tensor(op.outputs[index], name="tensor")
shape = val.get_shape()
if shape.is_fully_defined():
    # If the shape is known statically, just create a zero tensor with
    # the right shape in the grad loop context.
    if val.dtype == dtypes.resource:
        result = array_ops.zeros(
            resource_variable_ops.variable_shape(val),
            dtype=default_gradient.get_zeros_dtype(val))
    else:
        result = constant_op.constant(0, shape=shape.dims, dtype=val.dtype)
    if dead_branch:
        # op is a cond switch. Guard the zero tensor with a switch.
        pred = grad_state.history_map.get(op_ctxt.pred.name)
        branch = op_ctxt.branch
        result = control_flow_ops._SwitchRefOrTensor(result, pred)[1 - branch]
else:
    # Unknown shape so keep a history of the shape at runtime.
    if dead_branch:
        # Need to add a special switch to guard the value.
        pred = op_ctxt.pred
        branch = op_ctxt.branch
        op_ctxt.outer_context.Enter()
        val = control_flow_ops._SwitchRefOrTensor(op.inputs[0],
                                                  pred)[1 - branch]
        zeros_shape = array_ops.shape_internal(val, optimize=False)
        op_ctxt.outer_context.Exit()
        val.op._set_control_flow_context(op_ctxt)
        zeros_shape.op._set_control_flow_context(op_ctxt)
    else:
        op_ctxt.Enter()
        zeros_shape = array_ops.shape_internal(val, optimize=False)
        op_ctxt.Exit()

    # Add forward accumulator for shape.
    grad_state.grad_context.Exit()
    history_zeros_shape = grad_state.AddForwardAccumulator(
        zeros_shape, dead_branch=dead_branch)
    grad_state.grad_context.Enter()

    # Create a zero tensor with the right shape.
    shape = grad_state.AddBackpropAccumulatedValue(history_zeros_shape,
                                                   zeros_shape, dead_branch)
    result = array_ops.zeros(shape, val.dtype)
exit(result)
