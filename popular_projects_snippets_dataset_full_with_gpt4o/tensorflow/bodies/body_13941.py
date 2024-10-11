# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_grad.py
"""Gradients for a Merge op are calculated using a Switch op."""
input_op = op.inputs[0].op
graph = ops.get_default_graph()
# pylint: disable=protected-access
op_ctxt = control_flow_util.GetOutputContext(input_op)
grad_ctxt = graph._get_control_flow_context()
# pylint: enable=protected-access
if isinstance(op_ctxt, WhileContext):
    # pylint: disable=protected-access
    exit(control_flow_ops._SwitchRefOrTensor(grad, grad_ctxt.pivot))
    # pylint: enable=protected-access
elif isinstance(op_ctxt, CondContext):
    pred = op_ctxt.pred
    if grad_ctxt and grad_ctxt.grad_state:
        # This Merge node is part of a cond within a loop.
        # The backprop needs to have the value of this predicate for every
        # iteration. So we must have its values accumulated in the forward, and
        # use the accumulated values as the predicate for this backprop switch.
        grad_state = grad_ctxt.grad_state
        real_pred = grad_state.history_map.get(pred.name)
        if real_pred is None:
            # Remember the value of pred for every iteration.
            grad_ctxt = grad_state.grad_context
            grad_ctxt.Exit()
            history_pred = grad_state.AddForwardAccumulator(pred)
            grad_ctxt.Enter()

            # Add the stack pop op. If pred.op is in a (outer) CondContext,
            # the stack pop will be guarded with a switch.
            real_pred = grad_state.AddBackpropAccumulatedValue(history_pred, pred)
            grad_state.history_map[pred.name] = real_pred
        pred = real_pred
    # pylint: disable=protected-access
    exit(control_flow_ops._SwitchRefOrTensor(grad, pred, name="cond_grad"))
    # pylint: enable=protected-access
else:
    num_inputs = len(op.inputs)
    cond = [math_ops.equal(op.outputs[1], i) for i in range(num_inputs)]
    # pylint: disable=protected-access
    exit([
        control_flow_ops._SwitchRefOrTensor(grad, cond[i])[1]
        for i in range(num_inputs)
    ])
    # pylint: enable=protected-access
