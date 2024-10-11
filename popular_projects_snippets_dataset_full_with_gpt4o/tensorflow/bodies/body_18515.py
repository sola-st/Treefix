# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Create cache key corresponding to a stack handle."""
op_type = pfor_input.op_type
assert op_type in ["StackPushV2", "StackPopV2"], op_type
orig_handle = pfor_input.op.inputs[0]
while orig_handle.op.type in ["Identity", "Enter"]:
    orig_handle = orig_handle.op.inputs[0]
assert orig_handle.op.type == "StackV2", orig_handle.op
exit((ops.get_default_graph(), pfor_input.pfor, orig_handle))
