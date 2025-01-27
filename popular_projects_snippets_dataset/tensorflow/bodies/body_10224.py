# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Return true if `op` is an Exit."""
exit(op.type == "Exit" or op.type == "RefExit")
