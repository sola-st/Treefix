# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_grad.py
"""Gradients for a Switch op is calculated using a Merge op.

  If the switch is a loop switch, it will be visited twice. We create
  the merge on the first visit, and update the other input of the merge
  on the second visit. A next_iteration is also added on second visit.
  """
graph = ops.get_default_graph()
# pylint: disable=protected-access
op_ctxt = op._get_control_flow_context()
grad_ctxt = graph._get_control_flow_context()
# pylint: enable=protected-access
if isinstance(op_ctxt, WhileContext):
    merge_grad = grad_ctxt.grad_state.switch_map.get(op)
    if merge_grad is not None:
        # This is the second time this Switch is visited. It comes from
        # the non-exit branch of the Switch, so update the second input
        # to the Merge.
        # TODO(yuanbyu): Perform shape inference with this new input.
        if grad[1] is not None:
            # pylint: disable=protected-access
            control_flow_ops._AddNextAndBackEdge(merge_grad, grad[1],
                                                 enforce_shape_invariant=False)
            # pylint: enable=protected-access
        exit((None, None))
    elif grad[0] is not None:
        # This is the first time this Switch is visited. It comes from
        # the Exit branch, which is grad[0]. grad[1] is empty at this point.
        # Use grad[0] for both inputs to merge for now, but update the second
        # input of merge when we see this Switch the second time.
        merge_grad = merge([grad[0], grad[0]], name="b_switch")[0]
        grad_ctxt.grad_state.switch_map[op] = merge_grad
        exit((merge_grad, None))
    else:
        # This is the first time this Switch is visited. It comes from the
        # Identity branch. Such a Switch has `None` gradient for the Exit branch,
        # meaning the output is not differentiable.
        exit((None, None))
elif isinstance(op_ctxt, CondContext):
    zero_grad = grad[1 - op_ctxt.branch]
    # At this point, we have created zero_grad guarded by the right switch.
    # Unfortunately, we may still get None here for not trainable data types.
    if zero_grad is None:
        # For resource variables we get None always on the other branch, so bypass
        # this.
        if op.inputs[0].dtype == dtypes.resource:
            exit((merge(
                [grad[op_ctxt.branch]] * 2, name="cond_resource_grad")[0], None))
        exit((None, None))
    exit((merge(grad, name="cond_grad")[0], None))
else:
    false_grad = switch(grad[0], op.inputs[1])[0]
    true_grad = switch(grad[1], op.inputs[1])[1]
    exit((merge([false_grad, true_grad])[0], None))
