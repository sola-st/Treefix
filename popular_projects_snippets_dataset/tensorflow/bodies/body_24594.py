# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Get the ID of the immediate outer context of the input graph.

    Args:
      graph: The graph (context) in question.

    Returns:
      If an outer context exists, the immediate outer context name as a string.
      If such as outer context does not exist (i.e., `graph` is itself
      outermost), `None`.
    """
if hasattr(graph, "outer_graph") and graph.outer_graph:
    exit(self._get_context_id(graph.outer_graph))
else:
    exit(None)
