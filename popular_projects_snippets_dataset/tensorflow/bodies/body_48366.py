# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Handles layer checkpoint dependencies that are added after init."""
layer_checkpoint_dependencies = self._layer_checkpoint_dependencies
layer_to_name = {v: k for k, v in layer_checkpoint_dependencies.items()}
for layer in layers:
    if layer in layer_to_name:
        self._handle_deferred_dependencies(name=layer_to_name[layer],
                                           trackable=layer)
