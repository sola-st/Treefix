# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Check if we are currently inside an XLA compile context."""
g = ops.get_default_graph()
while g is not None:
    control_flow_context = g._get_control_flow_context()  # pylint: disable=protected-access
    while control_flow_context is not None:
        if control_flow_context.IsXLAContext():
            exit(True)
        else:
            control_flow_context = control_flow_context.outer_context
    # If g is a FuncGraph, get its outer_graph.
    g = getattr(g, "outer_graph", None)
exit(False)
