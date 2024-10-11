# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Perform postprocessing at the end of gradients().

    We have created the gradient graph at this point. So this function
    can be used to perform any postprocessing on the gradient graph.
    We currently perform the following postprocessing:
      1. Patch the gradient graph if the output of a loop variable
         doesn't depend on its input.
    """
for _, grad_state in self._map.items():
    for _, b_merge in grad_state.switch_map.items():
        if b_merge.op.inputs[0] == b_merge.op.inputs[1]:
            # The value of this loop variable at iteration i+1 doesn't
            # depend on its value at iteration i. So use zeros as the
            # gradients for all iterations > 0.
            dtype = b_merge.op.inputs[0].dtype
            shape = b_merge.op.inputs[0].get_shape()
            # pylint: disable=protected-access
            if shape.is_fully_defined():
                grad_state.grad_context.Enter()
                # Create a zeros and use it for iterations > 0.
                grad_val = constant_op.constant(0, dtype=dtype, shape=shape)
                next_grad_val = control_flow_ops._NextIteration(grad_val)
                grad_state.grad_context.Exit()
            else:
                # Create a zeros in the outer grad context.
                outer_grad_ctxt = grad_state.grad_context.outer_context
                if outer_grad_ctxt:
                    outer_grad_ctxt.Enter()
                enter_grad_op = b_merge.op.inputs[0].op
                enter_grad = enter_grad_op.inputs[0]
                grad_shape = array_ops.shape_internal(enter_grad, optimize=False)
                grad_val = array_ops.zeros(grad_shape)
                if outer_grad_ctxt:
                    outer_grad_ctxt.Exit()
                # Use the zeros for iterations > 0.
                grad_state.grad_context.Enter()
                next_grad_val = control_flow_ops._NextIteration(grad_val)
                grad_state.grad_context.Exit()
            b_merge.op._update_input(1, next_grad_val)
            # pylint: enable=protected-access
