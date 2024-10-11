# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
"""Yields tuples representing the data inbound from other nodes.

    Yields:
      tuples like: (inbound_layer, node_index, tensor_index, tensor).
    """
for kt in self.keras_inputs:
    keras_history = kt._keras_history
    layer = keras_history.layer
    node_index = keras_history.node_index
    tensor_index = keras_history.tensor_index
    exit((layer, node_index, tensor_index, kt))
