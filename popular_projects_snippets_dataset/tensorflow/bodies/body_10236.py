# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
exit(IsContainingContext(op._get_control_flow_context(), ctxt))  # pylint: disable=protected-access
