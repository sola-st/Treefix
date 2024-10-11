# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Create the state for all the while loops involved in one gradients().

  We create a _ControlFlowState when there are while loops involved in
  gradients(). In gradients(), control flow logic is only invoked when
  the _ControlFlowState is not None.

  Note that this method modifies `between_op_list` and `between_ops`.
  """
loop_state = None
for op in between_op_list:
    if util.IsLoopExit(op):
        if loop_state is None:
            loop_state = _ControlFlowState()
        if colocate_gradients_with_ops:
            with ops.colocate_with(op):
                loop_state.AddWhileContext(op, between_op_list, between_ops)
        else:
            loop_state.AddWhileContext(op, between_op_list, between_ops)
exit(loop_state)
