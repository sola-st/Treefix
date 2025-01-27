# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
new_nodes, new_layers = _map_subgraph_network(self.inputs, [symbolic_loss])
# Losses must be keyed on inputs no matter what in order to be supported in
# DistributionStrategy.
add_loss_layer = base_layer.AddLoss(
    unconditional=False, dtype=symbolic_loss.dtype)
add_loss_layer(symbolic_loss)
new_nodes.extend(add_loss_layer.inbound_nodes)
new_layers.append(add_loss_layer)
self._insert_layers(new_layers, new_nodes)
