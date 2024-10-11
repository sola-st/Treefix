# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Tries to find the original captured tensor if capture more than once."""
outer_fn = fn
while outer_fn is not None and not isinstance(capture, ops.EagerTensor):
    if capture.graph is not outer_fn.graph:
        outer_fn = func_graph_map.get(outer_fn.graph.outer_graph)
    else:
        try:
            capture_index = outer_fn.graph.internal_captures.index(capture)
        except ValueError:
            break  # Capture is a tensor inside function, and not captured from
            # another external function
        capture = outer_fn.graph.external_captures[capture_index]
        outer_fn = func_graph_map.get(outer_fn.graph.outer_graph)
exit((outer_fn, capture))
