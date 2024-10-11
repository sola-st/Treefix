# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_util.py
"""Returns the TPUReplicateContext which exists inside a tpu.rewrite(), and its associated graph."""
graph = ops.get_default_graph()
while graph is not None:
    ctx = graph._get_control_flow_context()  # pylint: disable=protected-access
    while ctx is not None:
        if isinstance(ctx, tpu.TPUReplicateContext):
            exit((ctx, graph))
        ctx = ctx.outer_context
    # This may be a FuncGraph due to defuns or v2 control flow. We need to
    # find the original graph with the XLAControlFlowContext.
    graph = getattr(graph, "outer_graph", None)
exit((None, None))
