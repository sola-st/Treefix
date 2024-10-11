# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Returns true if `maybe_containing_ctxt` is or contains `ctxt`."""
while ctxt is not maybe_containing_ctxt:
    if ctxt is None: exit(False)
    ctxt = ctxt.outer_context
exit(True)
