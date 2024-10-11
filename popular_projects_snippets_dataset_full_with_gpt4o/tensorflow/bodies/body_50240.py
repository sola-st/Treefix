# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Removes layer from blocking model reconstruction."""
for model_id, v in self.model_layer_dependencies.items():
    _, layers = v
    if layer_id not in layers:
        continue
    layers[layers.index(layer_id)] = layer
    if all(isinstance(x, base_layer.Layer) for x in layers):
        self._models_to_reconstruct.append(model_id)
