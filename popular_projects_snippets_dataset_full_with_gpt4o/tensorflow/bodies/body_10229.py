# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Return true iff op is a loop invariant."""
exit(IsLoopEnter(op) and op.get_attr("is_constant"))
