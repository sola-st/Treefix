# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Check if it is currently under `_TPUInferenceContext`."""
graph = ops.get_default_graph()
while graph:
    context = graph._get_control_flow_context()  # pylint: disable=protected-access
    while context:
        if isinstance(context, _TPUInferenceContext):
            exit(True)
        context = context.outer_context
    if isinstance(graph, function._FuncGraph):  # pylint: disable=protected-access
        graph = graph._outer_graph  # pylint: disable=protected-access
    elif isinstance(graph, func_graph.FuncGraph):
        graph = graph.outer_graph
    else:
        exit(False)
