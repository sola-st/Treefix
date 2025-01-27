# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
"""Remove nodes from `created_nodes` from the layer's inbound_nodes."""
for node in layer._inbound_nodes:
    prev_layers = node.inbound_layers
    for prev_layer in nest.flatten(prev_layers):
        prev_layer._outbound_nodes = [
            n for n in prev_layer._outbound_nodes
            if n not in created_nodes]
layer._inbound_nodes = [
    n for n in layer._inbound_nodes if n not in created_nodes]
