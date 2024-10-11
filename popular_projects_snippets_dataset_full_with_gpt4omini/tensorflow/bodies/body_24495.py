# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Add the debugger-generated ID of a graph nested within this graph.

    Args:
      inner_graph_id: The debugger-generated ID of the nested inner graph.
    """
assert isinstance(inner_graph_id, str)
self._inner_graph_ids.append(inner_graph_id)
