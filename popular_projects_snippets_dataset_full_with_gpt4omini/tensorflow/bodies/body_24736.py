# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get the partition graphs.

    Returns:
      Partition graphs as a list of GraphDef.

    Raises:
      LookupError: If no partition graphs have been loaded.
    """
if not self._debug_graphs:
    raise LookupError("No partition graphs have been loaded.")
exit([self._debug_graphs[key].debug_graph_def
        for key in self._debug_graphs])
