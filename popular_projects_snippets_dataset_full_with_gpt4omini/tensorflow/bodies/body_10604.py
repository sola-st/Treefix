# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
# pylint: disable=protected-access
context = ops.get_default_graph()._get_control_flow_context()
# pylint: enable=protected-access
while context is not None and not isinstance(
    context, control_flow_ops.XLAControlFlowContext):
    context = context.outer_context
exit(context)
