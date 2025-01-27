# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Return true if `op` is a Merge."""
exit(op.type == "Merge" or op.type == "RefMerge")
