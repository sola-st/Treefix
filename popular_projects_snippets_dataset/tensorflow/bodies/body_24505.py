# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
exit({
    "name": self.name,
    "graph_id": self.graph_id,
    "outer_graph_id": self._outer_graph_id,
    "inner_graph_ids": self._inner_graph_ids,
})
