# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Reconstructs the network structure."""
config = json_utils.decode(self._metadata[model_id].metadata)['config']

# Set up model inputs
if model.inputs:
    # Inputs may already be created if the model is instantiated in another
    # object's __init__.
    pass
elif isinstance(model, models_lib.Sequential):
    if not layers or not isinstance(layers[0], input_layer.InputLayer):
        if config['layers'][0]['class_name'] == 'InputLayer':
            layers.insert(0, input_layer.InputLayer.from_config(
                config['layers'][0]['config']))
        elif 'batch_input_shape' in config['layers'][0]['config']:
            batch_input_shape = config['layers'][0]['config']['batch_input_shape']
            layers.insert(0, input_layer.InputLayer(
                input_shape=batch_input_shape[1:],
                batch_size=batch_input_shape[0],
                dtype=layers[0].dtype,
                name=layers[0].name + '_input'))
    model.__init__(layers, name=config['name'])
    if not model.inputs:
        first_layer = self._get_child_layer_node_ids(model_id)[0]
        input_specs = self._infer_inputs(first_layer)
        input_shapes = self._infer_inputs(first_layer, convert_to_shapes=True)
        model._set_inputs(input_specs)  # pylint: disable=protected-access
        if not model.built and not isinstance(input_specs, dict):
            model.build(input_shapes)
else:  # Reconstruct functional model
    (inputs, outputs,
     created_layers) = functional_lib.reconstruct_from_config(
         config, created_layers={layer.name: layer for layer in layers})
    model.__init__(inputs, outputs, name=config['name'])
    functional_lib.connect_ancillary_layers(model, created_layers)

# Set model dtype.
_set_network_attributes_from_metadata(model)

# Unblock models that are dependent on this model.
self._unblock_model_reconstruction(model_id, model)
