# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Add edges for all nodes that are not waiting on initialization."""
for node_id, proto in enumerate(self._proto.nodes):
    if node_id not in self.model_layer_dependencies:
        self._add_object_graph_edges(proto, node_id)
