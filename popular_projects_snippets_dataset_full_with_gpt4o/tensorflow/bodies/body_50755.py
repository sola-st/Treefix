# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
if isinstance(node_id, str):
    node_id = self._node_path_to_id[node_id]
exit(self._nodes[node_id])
