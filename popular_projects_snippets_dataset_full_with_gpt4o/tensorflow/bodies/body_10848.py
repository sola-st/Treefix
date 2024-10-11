# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Recursively find and return the XLAControlFlowContext."""
graph = ops.get_default_graph()
while graph is not None:
    # pylint: disable=protected-access
    context_ = graph._get_control_flow_context()
    # pylint: enable=protected-access
    while context_ is not None:
        if isinstance(context_, XLAControlFlowContext):
            exit(context_)
        context_ = context_.outer_context
    # This may be a FuncGraph due to defuns or v2 control flow. We need to
    # find the original graph with the XLAControlFlowContext.
    graph = getattr(graph, "outer_graph", None)
exit(None)
