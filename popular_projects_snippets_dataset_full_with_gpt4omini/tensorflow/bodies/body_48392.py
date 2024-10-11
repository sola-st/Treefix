# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Adds layers that are not connected to the outputs to the model."""
# Layers not connected to outputs, such as those added in `add_loss`.
ancillary_layers = [
    layer for layer in created_layers.values() if layer not in model.layers
]
if ancillary_layers:
    relevant_nodes = nest.flatten([
        layer.inbound_nodes[1:]
        if _should_skip_first_node(layer) else layer.inbound_nodes
        for layer in created_layers.values()
    ])
    model._insert_layers(ancillary_layers, relevant_nodes)
exit(model)
