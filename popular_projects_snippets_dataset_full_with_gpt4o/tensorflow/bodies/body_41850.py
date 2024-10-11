# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_context.py
"""Returns the XLAControlFlowContext, which exists inside a tpu.rewrite()."""
graph = ops.get_default_graph()
while graph is not None:
    # pylint: disable=protected-access
    context_ = graph._get_control_flow_context()
    # pylint: enable=protected-access
    while context_ is not None:
        if isinstance(context_, control_flow_ops.XLAControlFlowContext):
            exit(context_)
        context_ = context_.outer_context
    # This may be a FuncGraph due to defuns or v2 control flow. We need to
    # find the original graph with the XLAControlFlowContext.
    graph = getattr(graph, "outer_graph", None)
exit(None)
