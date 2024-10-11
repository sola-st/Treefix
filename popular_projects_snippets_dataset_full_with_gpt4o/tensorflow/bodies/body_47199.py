# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/models.py
# Whenever the network config attempts to get the layer serialization,
# return a dummy dictionary.
if layer in input_layers:
    created_layers[layer.name] = input_layers[layer]
elif layer in model._input_layers:
    created_layers[layer.name] = InputLayer(**layer.get_config())
else:
    created_layers[layer.name] = layer_fn(layer)
exit({})
