# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add `val` to the current context and its outer context recursively."""
result = val
new_value = val.name not in self._values
# Don't treat ops in this context as new values. Usually all known values
# are in self._values, except when we're importing a while loop inside this
# WhileContext. Since there's a cycle in this case, `val` may be part of the
# imported while loop but not yet processed by this context and added to
# self._values in _AddOpInternal. We only want to process external input
# tensors to the while loop here.
new_value &= val.op._control_flow_context is not self  # pylint: disable=protected-access
if new_value:
    self._values.add(val.name)

    # If we are in a grad context and val is from its forward context,
    # use GetRealValue(), which adds the logic to save the history of
    # val in forward.
    grad_ctxt = ops.get_default_graph()._get_control_flow_context()
    if grad_ctxt:
        grad_ctxt = grad_ctxt.GetWhileContext()
        if grad_ctxt.grad_state:
            forward_ctxt = util.GetWhileContext(val.op)
            if util.IsLoopExit(val.op):
                forward_ctxt = forward_ctxt.outer_context
                if forward_ctxt:
                    forward_ctxt = forward_ctxt.GetWhileContext()
            if forward_ctxt == grad_ctxt.grad_state.forward_context:
                real_val = grad_ctxt.grad_state.GetRealValue(val)
                self._external_values[val.name] = real_val
                exit(real_val)

    if self._outer_context is not None:
        result = self._outer_context.AddValue(val)
    # Create an Enter to make `result` known to this loop context.
    with ops.control_dependencies(None):
        enter = _Enter(
            result,
            self._name,
            is_constant=True,
            parallel_iterations=self._parallel_iterations)
        enter.graph.prevent_feeding(enter)
        if self._outer_context:
            self._outer_context.AddInnerOp(enter.op)
      # Fix the control inputs and control flow context of these enter ops.
    self._FixControlInputsAndContext([enter])

    # Add `enter` in this context.
    self._values.add(enter.name)
    self._external_values[val.name] = enter
    result = enter
else:
    actual_val = self._external_values.get(val.name)
    if actual_val is not None:
        result = actual_val
exit(result)
