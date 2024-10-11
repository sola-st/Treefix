# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
ctxt = graph._get_control_flow_context()  # pylint: disable=protected-access
exit(GetContainingXLAContext(ctxt) is not None)
