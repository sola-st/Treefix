# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add `op` to the current context."""
# For a reduction op, if op is in a grad context and its input is from
# its forward context, moving op to the forward context means we would
# store the tensor after the reduction as opposed to the tensor before
# reduction, and therefore could significantly reduce memory consumption.
# For now, we do this only for a few ops.
#
# If in XLA context, do not move constant ops to forward pass as pushing to
# and popping from a stack removes the constant property of an op and breaks
# XLA compilation, which requires certain inputs to be constant for certain
# ops.
if not util.IsInXLAContext(op) and op.type in {"Shape", "Size", "Rank"}:
    grad_ctxt = ops.get_default_graph()._get_control_flow_context()
    if grad_ctxt:
        grad_ctxt = grad_ctxt.GetWhileContext()
        if grad_ctxt.grad_state:
            op_input_forward_ctxt = util.GetWhileContext(op.inputs[0].op)
            if op_input_forward_ctxt == grad_ctxt.grad_state.forward_context:
                op_input_ctxt = op.inputs[0].op._get_control_flow_context()
                op._set_control_flow_context(op_input_ctxt)
                op_input_ctxt._AddOpInternal(op)
                exit()
self._AddOpInternal(op)
