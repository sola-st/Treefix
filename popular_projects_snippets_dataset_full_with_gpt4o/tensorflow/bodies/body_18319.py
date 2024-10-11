# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Converts an Enter node."""
inp, stacked, _ = parent_pfor._convert_helper(enter.op.inputs[0])
control_inputs = []
for x in enter.op.control_inputs:
    converted = parent_pfor._convert_helper(x)
    if not isinstance(converted, ops.Operation):
        converted = converted.t
    control_inputs.append(converted)
if control_inputs:
    with ops.control_dependencies(control_inputs):
        inp = array_ops.identity(inp)
exit((inp, stacked))
