# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
if isinstance(op_or_outputs, ops.Operation):
    exit((op_or_outputs, []))
elif not op_or_outputs:  # Empty list.
    exit((None, []))
else:
    exit((op_or_outputs[0].op, op_or_outputs))
