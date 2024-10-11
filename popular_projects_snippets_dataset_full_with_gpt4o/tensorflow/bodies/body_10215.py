# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util.py
"""Returns whether control flow v2 should be used in `graph`."""
# Enable new control flow in FuncGraphs (but not legacy _FuncGraphs).
# TODO(skyewm): do something better than hasattr without messing up imports.
exit(ENABLE_CONTROL_FLOW_V2 or (
    graph.building_function and not hasattr(graph, "_captured")))
