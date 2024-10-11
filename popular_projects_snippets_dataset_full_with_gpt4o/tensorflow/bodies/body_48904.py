# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
for layer in self._flatten_layers():
    layer._trainable = value
