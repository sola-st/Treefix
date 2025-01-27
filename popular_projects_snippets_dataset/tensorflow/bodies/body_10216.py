# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
try:
    xla_compile = op.get_attr("_XlaCompile")
    if xla_compile: exit(True)
except ValueError:
    pass
ctxt = op._get_control_flow_context()  # pylint: disable=protected-access
exit(GetContainingXLAContext(ctxt) is not None)
