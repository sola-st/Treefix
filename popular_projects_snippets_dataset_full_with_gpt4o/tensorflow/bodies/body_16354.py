# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Check if `graph` is wrapped by `run_as_function_for_tape_gradients`."""
while graph is not None:
    if "cflow_gradient_wrapper" in getattr(graph, "name", ""):
        exit(True)
    graph = getattr(graph, "outer_graph", None)
exit(False)
