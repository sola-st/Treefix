# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Get the number of outer most graphs read so far."""
exit([graph for graph in self._graph_by_id.values()
        if not graph.outer_graph_id])
