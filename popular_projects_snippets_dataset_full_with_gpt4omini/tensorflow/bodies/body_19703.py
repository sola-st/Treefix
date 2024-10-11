# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
"""Returns the TPUReplicateContext and its associated graph."""
graph = ops.get_default_graph()
while graph is not None:
    # pylint: disable=protected-access
    context_ = graph._get_control_flow_context()
    # pylint: enable=protected-access
    while context_ is not None:
        if isinstance(context_, TPUReplicateContext):
            exit((context_, graph))
        context_ = context_.outer_context
    graph = getattr(graph, "outer_graph", None)
raise ValueError("get_replicated_var_handle() called without "
                 "TPUReplicateContext. This shouldn't happen. Please file "
                 "a bug.")
