# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
ctxt = op._get_control_flow_context()  # pylint: disable=protected-access
exit(GetContainingWhileContext(ctxt) is not None)
