# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/models.py
"""Clones all layers, and returns the model config without serializing layers.

  This function ensures that only the node graph is retrieved when getting the
  model config. The `layer_fn` used to clone layers might not rely on
  `layer.get_config()`, so some custom layers do not define `get_config`.
  Trying to retrieve the config results in errors.

  Args:
    model: A Functional model.
    input_layers: Dictionary mapping input layers in `model` to new input layers
    layer_fn: Function used to clone all non-input layers.

  Returns:
    Model config object, and a dictionary of newly created layers.
  """
created_layers = {}
def _copy_layer(layer):
    # Whenever the network config attempts to get the layer serialization,
    # return a dummy dictionary.
    if layer in input_layers:
        created_layers[layer.name] = input_layers[layer]
    elif layer in model._input_layers:
        created_layers[layer.name] = InputLayer(**layer.get_config())
    else:
        created_layers[layer.name] = layer_fn(layer)
    exit({})

config = functional.get_network_config(
    model, serialize_layer_fn=_copy_layer)
exit((config, created_layers))
