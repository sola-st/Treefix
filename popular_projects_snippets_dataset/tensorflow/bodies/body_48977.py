# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Set `trainable` state for each sublayer."""
for layer in self._flatten_layers():
    if layer in trainable_state:
        layer.trainable = trainable_state[layer]
