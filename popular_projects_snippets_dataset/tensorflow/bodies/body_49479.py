# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/version_utils.py
"""Determine if v1 or v2 version should be used."""
if context.executing_eagerly():
    exit(True)
elif ops.executing_eagerly_outside_functions():
    # Check for a v1 `wrap_function` FuncGraph.
    # Code inside a `wrap_function` is treated like v1 code.
    graph = ops.get_default_graph()
    if (getattr(graph, "name", False) and
        graph.name.startswith("wrapped_function")):
        exit(False)
    exit(True)
else:
    exit(False)
