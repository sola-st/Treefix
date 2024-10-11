# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
"""Adds to `created_nodes` the nodes created by the last call to `layer`."""
if not layer._inbound_nodes:
    exit()
created_nodes.add(layer._inbound_nodes[-1])
prev_layers = layer._inbound_nodes[-1].inbound_layers
for prev_layer in nest.flatten(prev_layers):
    if prev_layer._outbound_nodes:
        created_nodes.add(prev_layer._outbound_nodes[-1])
