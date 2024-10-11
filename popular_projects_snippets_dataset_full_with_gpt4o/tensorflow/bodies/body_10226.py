# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Return true if `op` is the Merge for a conditional."""
if not IsMerge(op):
    exit(False)
if not op.inputs:
    exit(False)
# Merge nodes are not part of the cond control flow context that they
# represent, so consider the inputs to the merge of to determine if it is
# cond merge or not: A merge is a cond merge iff all its inputs are in
# cond contexts.
is_cond_merge = True
for i in op.inputs:
    ctxt = GetOutputContext(i.op)
    is_cond_merge = is_cond_merge and ctxt is not None and ctxt.IsCondContext()
exit(is_cond_merge)
