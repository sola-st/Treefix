# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Add the grad state for the while loop that op belongs to.

    Note that op is an Exit, and this method must be called in
    the control flow context where gradients() is called.

    Note that this method modifies `between_op_list` and `between_ops`.
    """
forward_ctxt = util.GetWhileContext(op)
grad_state = self._map.get(forward_ctxt)
if grad_state is None:
    # This is a new while loop so create a grad state for it.
    outer_forward_ctxt = forward_ctxt.outer_context
    if outer_forward_ctxt:
        outer_forward_ctxt = outer_forward_ctxt.GetWhileContext()
    outer_grad_state = None
    if outer_forward_ctxt:
        outer_grad_state = self._map.get(outer_forward_ctxt)
    grad_state = _GradLoopState(forward_ctxt, outer_grad_state)
    self._map[forward_ctxt] = grad_state

    # We need to include all exits of a loop for backprop.
    for loop_exit in grad_state.forward_loop_exits:
        if loop_exit.op not in between_ops:
            between_ops.add(loop_exit.op)
            between_op_list.append(loop_exit.op)
