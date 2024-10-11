# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Returns True if handle was created inside the pfor loop."""
# We use some heuristic to find the original TensorArray creation op.
# The logic should handle the common cases (except cond based subgraphs).
# In theory the user could perform different operations on the handle (like
# Reshape, stack multiple handles, etc) which could break this logic.
# TODO(agarwal): handle Switch/Merge.
while handle.op.type in ("Enter", "Identity"):
    handle = handle.op.inputs[0]
if handle.op.type not in [
    "TensorArrayV3", "TensorArrayGradV3", "TensorArrayGradWithShape"
]:
    raise ValueError(f"Unable to find source for handle {handle}.")
else:
    exit(pfor_input.pfor.op_is_inside_loop(handle.op))
