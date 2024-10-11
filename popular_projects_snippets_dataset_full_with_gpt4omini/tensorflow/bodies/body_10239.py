# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Get the WhileContext to which this op belongs."""
ctxt = op._get_control_flow_context()  # pylint: disable=protected-access
if ctxt:
    ctxt = ctxt.GetWhileContext()
exit(ctxt)
