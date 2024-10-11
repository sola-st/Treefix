# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
if input_shape is None or not self.layers:
    exit()
if not tf2.enabled() or not ops.executing_eagerly_outside_functions():
    # This behavior is disabled in V1 or when eager execution is disabled.
    exit()
if (not self._has_explicit_input_shape and
    not self._use_legacy_deferred_behavior):
    # Determine whether the input shape is novel, i.e. whether the model
    # should be rebuilt.
    input_shape = tuple(input_shape)
    if self._inferred_input_shape is None:
        new_shape = input_shape
    else:
        new_shape = relax_input_shape(self._inferred_input_shape, input_shape)
    if (new_shape is not None and new_shape != self._inferred_input_shape):
        # A novel shape has been received: we need to rebuild the model.
        # In case we are inside a graph function, we step out of it.
        with ops.init_scope():
            inputs = input_layer.Input(
                batch_shape=new_shape,
                dtype=input_dtype,
                name=self.layers[0].name + '_input')
            layer_input = inputs
            created_nodes = set()
            for layer in self.layers:
                # Clear nodes previously created via this method. This prevents
                # node accumulation and ensures that e.g. `layer.output` is
                # always connected to `model.inputs`
                # (this is important e.g. for the feature extraction use case).
                # We don't just do `layer._inbound_nodes = []` in order
                # not to break shared layers added to Sequential models (which is
                # technically illegal as per the `add()` docstring,
                # but wasn't previously disabled).
                clear_previously_created_nodes(layer, self._created_nodes)
                try:
                    # Create Functional API connection by calling the current layer
                    layer_output = layer(layer_input)
                except:  # pylint:disable=bare-except
                    # Functional API calls may fail for a number of reasons:
                    # 1) The layer may be buggy. In this case it will be easier for
                    # the user to debug if we fail on the first call on concrete data,
                    # instead of our own call on a symbolic input.
                    # 2) The layer is dynamic (graph-incompatible) and hasn't
                    # overridden `compute_output_shape`. In this case, it is
                    # impossible to build a graph network.
                    # 3) The layer is otherwise incompatible with the Functional API
                    # (e.g. this is the case for some probabilistic layers that rely
                    # on hacks and that do not return tensors).
                    # In all these cases, we should avoid creating a graph network
                    # (or we simply can't).
                    self._use_legacy_deferred_behavior = True
                    exit()
                if len(nest.flatten(layer_output)) != 1:
                    raise ValueError(SINGLE_LAYER_OUTPUT_ERROR_MSG)
                # Keep track of nodes just created above
                track_nodes_created_by_last_call(layer, created_nodes)
                layer_input = layer_output
                outputs = layer_output
            self._created_nodes = created_nodes
            try:
                # Initialize a graph Network. This call will never fail for
                # a stack of valid Keras layers.
                # However some users have layers that are fundamentally incompatible
                # with the Functional API, which do not return tensors. In this
                # case, we fall back to the legacy deferred behavior.
                # TODO(fchollet): consider raising here, as we should not be
                # supporting such layers.
                self._init_graph_network(inputs, outputs)
                self._graph_initialized = True
            except:  # pylint:disable=bare-except
                self._use_legacy_deferred_behavior = True
        self._inferred_input_shape = new_shape
