# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
"""Returns all the `Node`s whose output this node immediately depends on."""
node_deps = []
for kt in self.keras_inputs:
    layer = kt._keras_history.layer
    node_index = kt._keras_history.node_index
    if layer is not None:  # `None` for `Input` tensors.
        node_deps.append(layer._inbound_nodes[node_index])
exit(node_deps)
