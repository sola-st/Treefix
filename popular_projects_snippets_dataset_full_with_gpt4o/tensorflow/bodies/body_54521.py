# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Type-checks and possibly canonicalizes `graph_def`."""
if not isinstance(graph_def, graph_pb2.GraphDef):
    # `graph_def` could be a dynamically-created message, so try a duck-typed
    # approach
    try:
        old_graph_def = graph_def
        graph_def = graph_pb2.GraphDef()
        graph_def.MergeFrom(old_graph_def)
    except TypeError:
        raise TypeError('Argument `graph_def` must be a GraphDef proto.')
else:
    # If we're using the graph_def provided by the caller, modify graph_def
    # in-place to add attr defaults to the NodeDefs (this is visible to the
    # caller).
    # NOTE(skyewm): this is undocumented behavior that at least meta_graph.py
    # depends on. It might make sense to move this to meta_graph.py and have
    # import_graph_def not modify the graph_def argument (we'd have to make sure
    # this doesn't break anything else.)
    for node in graph_def.node:
        op_def = op_def_registry.get(node.op)
        if op_def is None:
            # Assume unrecognized ops are functions for now. TF_ImportGraphDef will
            # report an error if the op is actually missing.
            continue
        _SetDefaultAttrValues(node, op_def)

exit(graph_def)
