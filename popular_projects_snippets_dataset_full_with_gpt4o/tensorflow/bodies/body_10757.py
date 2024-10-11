# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Remove any external control dependency on this op."""
while_ctxt = self.GetWhileContext()
# A control input of `op` is internal if it is in the same while
# loop context as the enclosing while loop context of self.
if while_ctxt is None:
    internal_control_inputs, external_control_inputs = op.control_inputs, []
else:
    internal_control_inputs, external_control_inputs = [], []
    for x in op.control_inputs:
        ctxt = util.GetOutputContext(x)
        if ctxt is not None and ctxt.GetWhileContext() == while_ctxt:
            internal_control_inputs.append(x)
        else:
            external_control_inputs.append(x)
if len(internal_control_inputs) != len(op.control_inputs):
    # TODO(mdan): perhaps there should be a replace_control_inputs()
    op._remove_all_control_inputs()
    op._add_control_inputs(internal_control_inputs)
exit((internal_control_inputs, external_control_inputs))
