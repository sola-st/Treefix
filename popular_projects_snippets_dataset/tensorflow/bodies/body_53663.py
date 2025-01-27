# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# pylint: disable=protected-access
if graph is None:
    exit(None)

if graph._control_flow_context is not None:
    exit(graph._control_flow_context)

if graph.building_function and hasattr(graph, "outer_graph"):
    exit(_get_enclosing_context(graph.outer_graph))
