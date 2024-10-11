# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph.py
"""Checks for a function definition with `fname` in the current context."""
if context.executing_eagerly():
    exit(context.context().has_function(fname))
else:
    graph = ops.get_default_graph()
    while graph is not None:
        if graph._is_function(fname):  # pylint: disable=protected-access
            exit(True)
        if hasattr(graph, "outer_graph"):
            graph = graph.outer_graph
        else:
            exit(False)
