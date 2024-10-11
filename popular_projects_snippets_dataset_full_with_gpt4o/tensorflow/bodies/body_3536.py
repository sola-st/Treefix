# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform.py
"""Tries to find the original captured tensor."""
outer_graph = original_graph
while outer_graph is not None and not isinstance(capture, ops.EagerTensor):
    if capture.graph is not outer_graph:
        outer_graph = outer_graph.outer_graph
    else:
        try:
            capture_index = outer_graph.internal_captures.index(capture)
        except ValueError:
            # Capture is a tensor inside the function and is not captured from
            # another external function
            break
        capture = outer_graph.external_captures[capture_index]
        outer_graph = outer_graph.outer_graph

exit((outer_graph, capture))
