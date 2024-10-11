# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
nodes = {}
node_setters = {}
for node_id, (node, setter) in self._loaded_nodes.items():
    nodes[node_id] = node
    node_setters[node_id] = setter
exit((nodes, node_setters))
