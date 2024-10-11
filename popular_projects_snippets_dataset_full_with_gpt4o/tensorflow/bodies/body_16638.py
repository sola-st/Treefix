# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Create zeros_like gradient for a loop exit.

    If the result of a loop variable is not used but is involved in
    computing the result of some needed loop variable, we create a
    zero-valued tensor that is fed as gradient for the Exit node of that
    loop variable. Note that val.op is an Exit, and this method must be
    called in the control flow context where gradients() is called.

    Args:
      val: The output tensor of an Exit op.

    Returns:
      A zero tensor of the same shape of val.
    """
val_shape = val.get_shape()
forward_ctxt = val.op._get_control_flow_context()
outer_forward_ctxt = forward_ctxt.outer_context
if outer_forward_ctxt:
    outer_forward_ctxt = outer_forward_ctxt.GetWhileContext()
outer_grad_state = None
if outer_forward_ctxt:
    outer_grad_state = self._map.get(outer_forward_ctxt)
if outer_grad_state:
    # This is a nested loop.
    if val_shape.is_fully_defined():
        # If the shape is known statically, just create a zero tensor
        # with the right shape in the right context.
        outer_grad_state.grad_context.Enter()
        result = array_ops.zeros(val_shape.dims, val.dtype)
        outer_grad_state.grad_context.Exit()
    else:
        # Only the shape of value is needed for backprop.
        forward_ctxt.outer_context.Enter()
        shape = array_ops.shape_internal(val, optimize=False)
        forward_ctxt.outer_context.Exit()
        # Save the shape to a stack.
        history_shape = outer_grad_state.AddForwardAccumulator(shape)
        # Get the shape back from the stack.
        outer_grad_ctxt = outer_grad_state.grad_context
        outer_grad_ctxt.Enter()
        real_shape = outer_grad_state.AddBackpropAccumulatedValue(
            history_shape, shape)
        result = array_ops.zeros(real_shape, val.dtype)
        outer_grad_ctxt.Exit()
else:
    # This is not a nested loop.
    if val_shape.is_fully_defined():
        # If the shape is known statically, just create a zero tensor
        # with the right shape.
        result = array_ops.zeros(val_shape.dims, val.dtype)
    else:
        result = array_ops.zeros_like(val, optimize=False)
exit(result)
