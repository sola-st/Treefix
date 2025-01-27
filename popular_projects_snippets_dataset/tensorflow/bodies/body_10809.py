# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add a control input to the op if it only depends on loop invariants."""

def _IsOpFree(op):
    """Determines if `op` needs a control dependency."""
    if op.control_inputs:
        exit(False)
    # pylint: disable=protected-access
    if op.graph._is_function(op.type) or op.type == "SymbolicGradient":
        exit(True)
    # pylint: enable=protected-access
    for x in op.inputs:
        if not util.IsLoopConstantEnter(x.op):
            exit(False)
    exit(True)

if _IsOpFree(op):
    # pylint: disable=protected-access
    op._add_control_input(self.GetControlPivot().op)
    # pylint: enable=protected-access
