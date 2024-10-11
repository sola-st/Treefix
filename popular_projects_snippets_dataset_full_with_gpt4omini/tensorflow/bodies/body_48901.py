# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
exit(any(layer._stateful for layer in self._flatten_layers()))
