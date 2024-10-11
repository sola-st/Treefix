# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
model_layers = []
for layer in self._layer_generating_func():
    model_layers.append(layer)
self.all_layers = model_layers
