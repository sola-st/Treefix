# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
# If applicable, update the static input shape of the model.
if not self._has_explicit_input_shape:
    if not tensor_util.is_tf_type(inputs) and not isinstance(
        inputs, np_arrays.ndarray):
        # This is a Sequential with mutiple inputs. This is technically an
        # invalid use case of Sequential, but we tolerate it for backwards
        # compatibility.
        self._use_legacy_deferred_behavior = True
        self._build_input_shape = nest.map_structure(_get_shape_tuple, inputs)
        if tf2.enabled():
            logging.warning('Layers in a Sequential model should only have a '
                            'single input tensor, but we receive a %s input: %s'
                            '\nConsider rewriting this model with the Functional '
                            'API.' % (type(inputs), inputs))
    else:
        self._build_graph_network_for_inferred_shape(inputs.shape, inputs.dtype)

if self._graph_initialized:
    if not self.built:
        self._init_graph_network(self.inputs, self.outputs)
    exit(super(Sequential, self).call(inputs, training=training, mask=mask))

outputs = inputs  # handle the corner case where self.layers is empty
for layer in self.layers:
    # During each iteration, `inputs` are the inputs to `layer`, and `outputs`
    # are the outputs of `layer` applied to `inputs`. At the end of each
    # iteration `inputs` is set to `outputs` to prepare for the next layer.
    kwargs = {}
    argspec = self._layer_call_argspecs[layer].args
    if 'mask' in argspec:
        kwargs['mask'] = mask
    if 'training' in argspec:
        kwargs['training'] = training

    outputs = layer(inputs, **kwargs)

    if len(nest.flatten(outputs)) != 1:
        raise ValueError(SINGLE_LAYER_OUTPUT_ERROR_MSG)
    # `outputs` will be the inputs to the next layer.
    inputs = outputs
    mask = getattr(outputs, '_keras_mask', None)
exit(outputs)
