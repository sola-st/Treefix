# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
"""Adds a layer instance on top of the layer stack.

    Args:
        layer: layer instance.

    Raises:
        TypeError: If `layer` is not a layer instance.
        ValueError: In case the `layer` argument does not
            know its input shape.
        ValueError: In case the `layer` argument has
            multiple output tensors, or is already connected
            somewhere else (forbidden in `Sequential` models).
    """
# If we are passed a Keras tensor created by keras.Input(), we can extract
# the input layer from its keras history and use that without any loss of
# generality.
if hasattr(layer, '_keras_history'):
    origin_layer = layer._keras_history[0]
    if isinstance(origin_layer, input_layer.InputLayer):
        layer = origin_layer
        logging.warning(
            'Please add `keras.layers.InputLayer` instead of `keras.Input` to '
            'Sequential model. `keras.Input` is intended to be used by '
            'Functional model.')

if isinstance(layer, module.Module):
    if not isinstance(layer, base_layer.Layer):
        layer = functional.ModuleWrapper(layer)
else:
    raise TypeError('The added layer must be '
                    'an instance of class Layer. '
                    'Found: ' + str(layer))

tf_utils.assert_no_legacy_layers([layer])
if not self._is_layer_name_unique(layer):
    raise ValueError('All layers added to a Sequential model '
                     'should have unique names. Name "%s" is already the name'
                     ' of a layer in this model. Update the `name` argument '
                     'to pass a unique name.' % (layer.name,))

self.built = False
set_inputs = False
self._maybe_create_attribute('_self_tracked_trackables', [])
if not self._self_tracked_trackables:
    if isinstance(layer, input_layer.InputLayer):
        # Case where the user passes an Input or InputLayer layer via `add`.
        set_inputs = True
    else:
        batch_shape, dtype = training_utils.get_input_shape_and_dtype(layer)
        if batch_shape:
            # Instantiate an input layer.
            x = input_layer.Input(
                batch_shape=batch_shape, dtype=dtype, name=layer.name + '_input')
            # This will build the current layer
            # and create the node connecting the current layer
            # to the input layer we just created.
            layer(x)
            set_inputs = True

    if set_inputs:
        outputs = nest.flatten(layer._inbound_nodes[-1].outputs)
        if len(outputs) != 1:
            raise ValueError(SINGLE_LAYER_OUTPUT_ERROR_MSG)
        self.outputs = outputs
        self.inputs = layer_utils.get_source_inputs(self.outputs[0])
        self.built = True
        self._has_explicit_input_shape = True

elif self.outputs:
    # If the model is being built continuously on top of an input layer:
    # refresh its output.
    output_tensor = layer(self.outputs[0])
    if len(nest.flatten(output_tensor)) != 1:
        raise ValueError(SINGLE_LAYER_OUTPUT_ERROR_MSG)
    self.outputs = [output_tensor]
    self.built = True

if set_inputs or self._graph_initialized:
    self._init_graph_network(self.inputs, self.outputs)
    self._graph_initialized = True
else:
    self._self_tracked_trackables.append(layer)
    self._handle_deferred_layer_dependencies([layer])

self._layer_call_argspecs[layer] = tf_inspect.getfullargspec(layer.call)
