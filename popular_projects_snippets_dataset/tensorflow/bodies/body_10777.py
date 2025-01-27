# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add `op` to the current context."""
if not op.inputs:
    # If we're in a while loop, remove any control inputs from outside the
    # loop.
    self._RemoveExternalControlEdges(op)

    if not any(
        util.OpInContext(input_op, self) for input_op in op.control_inputs):
        # pylint: disable=protected-access
        op._add_control_input(self._pivot.op)
        # pylint: enable=protected-access
else:
    # Make each input to 'op' available in this CondContext. If an input is
    # already part of this context there's nothing to do, but if it's
    # external, AddValue() will handle adding the appropriate Switch node and
    # other bookkeeping.
    for index in range(len(op.inputs)):
        x = op.inputs[index]
        if op.type == "Merge" and x.op.type == "NextIteration":
            # Edge case: if we're importing a while loop inside this CondContext,
            # AddValue() will not correctly handle the NextIteration inputs to
            # Merge node. The problem is that the NextIteration should also be
            # part of this context, but if we're importing it won't have been
            # processed and added to the context yet, so AddValue() will try to
            # add a Switch which results in an invalid graph. Instead, we use the
            # NextIteration input as-is here, and it will eventually be added to
            # the context via AddOp().
            real_x = x
        else:
            real_x = self.AddValue(x)
        if real_x != x:
            # pylint: disable=protected-access
            op._update_input(index, real_x)
            # pylint: enable=protected-access
      # Remove any external control dependency on this op.
    self._RemoveExternalControlEdges(op)
    # pylint: disable=protected-access
    if op.graph._is_function(op.type) or op.type == "SymbolicGradient":
        op._add_control_input(self._pivot.op)
    # pylint: enable=protected-access

    # Mark op's outputs as seen by this context and any outer contexts.
output_names = [x.name for x in op.outputs]
ctxt = self
while ctxt is not None:
    # pylint: disable=protected-access
    ctxt._values.update(output_names)
    ctxt = ctxt._outer_context
    # pylint: enable=protected-access

if self._outer_context or not util.IsLoopExit(op):
    op.graph.prevent_fetching(op)

if self._outer_context:
    self._outer_context.AddInnerOp(op)
