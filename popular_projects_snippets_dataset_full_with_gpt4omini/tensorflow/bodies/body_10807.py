# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add `op` to the current context.

    We move any external control dependencies of the op to the loop pivot, to
    ensure they get executed.
    """
# This is needed to prevent frame mismatch errors where there are Const
# nodes inside tf.function in v1 while_loop and inlining is turned on.
if op.type in ["PartitionedCall", "StatefulPartitionedCall"]:
    op._add_control_input(self.GetControlPivot().op)  # pylint: disable=protected-access
if not op.inputs:
    # Remove any external control dependency on this op
    control_inputs, external_inputs = self._RemoveExternalControlEdges(op)
    # Add a control edge from the control pivot to this op.
    if not control_inputs:
        # pylint: disable=protected-access
        op._add_control_input(self.GetControlPivot().op)
        # pylint: enable=protected-access
    for x in op.outputs:
        self._values.add(x.name)
else:
    for index in range(len(op.inputs)):
        x = op.inputs[index]
        real_x = self.AddValue(x)
        if real_x != x:
            op._update_input(index, real_x)  # pylint: disable=protected-access
      # Remove any external control dependency on this op.
    _, external_inputs = self._RemoveExternalControlEdges(op)
    # Add a control dependency to prevent loop invariants from
    # enabling ops that should not be executed.
    self._MaybeAddControlDependency(op)
    for x in op.outputs:
        self._values.add(x.name)
if external_inputs:
    # Use an identity to pull control inputs as data inputs. Note that we
    # ignore ops which don't have outputs. TODO(apassos): fix that
    with ops.control_dependencies(None):
        self.Enter()
        external_inputs = [
            array_ops.identity(x.outputs[0]).op
            for x in external_inputs
            if x.outputs
        ]
        self.Exit()
    op._add_control_inputs(external_inputs)  # pylint: disable=protected-access
if self._outer_context or not util.IsLoopExit(op):
    op.graph.prevent_fetching(op)
    for x in op.outputs:
        op.graph.prevent_feeding(x)

if self._outer_context:
    self._outer_context.AddInnerOp(op)
