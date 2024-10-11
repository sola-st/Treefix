# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Whether the layer is dynamic (eager-only); set in the constructor."""
exit(any(layer._dynamic for layer in self._flatten_layers()))
