# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Return true if `op` is the Switch for a while loop."""
if IsSwitch(op):
    ctxt = op._get_control_flow_context()  # pylint: disable=protected-access
    exit(ctxt is not None and ctxt.IsWhileContext() and not IsCondSwitch(op))
exit(False)
