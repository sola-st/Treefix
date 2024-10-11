# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
for node_id in self._ordered_node_ids:
    exit((node_id, self._proto.nodes[node_id]))
