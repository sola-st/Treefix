# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Get the real value of `value`.

    If backprop "uses" a value produced by forward inference, an accumulator
    is added in the forward loop to accumulate its values.  We use the
    accumulated value. This method must be called in the grad loop context.
    `value` must be in forward and needed for backprop.

    Args:
      value: A tensor to be captured.

    Returns:
      The same tensor obtained from the saved history.
    """
assert value.op.type not in ["Variable", "VariableV2"]
real_value = self._history_map.get(value.name)
if real_value is None:
    cur_value = value
    cur_grad_state = self
    while True:
        enter_op = util.GetLoopConstantEnter(cur_value)
        if enter_op:
            # Special case: cur_value comes from a constant Enter node.
            cur_value = enter_op.inputs[0]
            cur_grad_state = cur_grad_state.outer_grad_state
            if cur_grad_state is None:
                # We are now outside all nested loops for this gradient(),
                # so `value` is a loop invariant and there is no need to
                # save the history of value. Just make cur_value to enter
                # the right control flow context.
                real_value = self._grad_context.AddValue(cur_value)
                break
        elif constant_op.is_constant(cur_value):
            # If the value to be forwarded is a constant, clone the constant in
            # the gradient loop rather than using a stack.
            # TODO(phawkins): consider hoisting the constant out of the loop
            # instead.
            real_value = constant_op.constant(
                tensor_util.constant_value(cur_value), dtype=cur_value.dtype)
            break
        else:
            # Record the history of this value in forward_ctxt.
            self._grad_context.Exit()
            history_value = cur_grad_state.AddForwardAccumulator(cur_value)
            self._grad_context.Enter()
            break

    if real_value is None:
        # Add the stack pop op in the grad context.
        real_value = cur_grad_state.AddBackpropAccumulatedValue(
            history_value, cur_value)
        if cur_grad_state != self:
            real_value = self._grad_context.AddValue(real_value)
    self._history_map[value.name] = real_value
exit(real_value)
