# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Remove any external control dependency on this op."""
internal_control_inputs = []
external_control_inputs = []
for x in op.control_inputs:
    # pylint: disable=protected-access
    is_internal_op = False
    ctxt = x._get_control_flow_context()
    while ctxt is not None:
        if ctxt == self:
            is_internal_op = True
            break
        ctxt = ctxt._outer_context
    if is_internal_op:
        internal_control_inputs.append(x)
    else:
        external_control_inputs.append(x)
    # pylint: enable=protected-access
    # pylint: disable=protected-access
op._remove_all_control_inputs()
op._add_control_inputs(internal_control_inputs)
# pylint: enable=protected-access
exit((internal_control_inputs, external_control_inputs))
