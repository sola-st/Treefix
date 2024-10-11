# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the parent graph or dummy eager object."""
# TODO(b/149317164): Currently FuncGraphs use ops.get_default_graph() as the
# outer graph. This results in outer_graph always being a Graph,
# even in eager mode (get_default_graph will create a new Graph if there
# isn't a default graph). Because of this bug, we have to specially set the
# key when eager execution is enabled.
parent_graph = graph.outer_graph
if (not isinstance(parent_graph, func_graph.FuncGraph) and
    ops.executing_eagerly_outside_functions()):
    exit(_DUMMY_EAGER_GRAPH.key)
exit(parent_graph)
