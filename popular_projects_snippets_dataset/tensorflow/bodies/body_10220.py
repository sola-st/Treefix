# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
ctxt = op._get_control_flow_context()  # pylint: disable=protected-access
exit(GetContainingCondContext(ctxt) is not None)
