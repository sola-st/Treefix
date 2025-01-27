# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
call_args = [] if call_args is None else call_args
call_kwargs = {} if call_kwargs is None else call_kwargs
outputs = [] if outputs is None else outputs

self.layer = layer
self.is_input = not call_args and not call_kwargs

# These arguments are user-provided. Copy the structures here so that
# future user modifications do not affect the node's metadata.
# We copy using map_structure rather than python's shallow or deep copy,
# because the args can be data structures (so shallow copy is
# insufficient), but individual values might not support copy.copy
# or be too expensive to deep copy.
call_args = nest.map_structure(lambda t: t, call_args)
call_kwargs = nest.map_structure(lambda t: t, call_kwargs)
self.outputs = nest.map_structure(lambda t: t, outputs)
self.call_args = call_args
self.call_kwargs = call_kwargs

# Cached for performance.
self._flat_arguments = nest.flatten((self.call_args, self.call_kwargs))
# Used to avoid expensive `nest` operations in the most common case.
self._single_positional_tensor_passed = (not self.call_kwargs and len(
    self.call_args) == 1 and tensor_util.is_tf_type(self.call_args[0]))

if not ops.executing_eagerly_outside_functions():
    # Create TensorFlowOpLayers if needed (in TF1)
    for obj in self._flat_arguments:
        if (isinstance(obj, ops.Tensor) and
            base_layer_utils.needs_keras_history(
                obj, ignore_call_context=True)):
            base_layer_utils.create_keras_history(obj)

self._keras_inputs = []
self._keras_inputs_ids_and_indices = []
for i, ele in enumerate(self._flat_arguments):
    if is_keras_tensor(ele):
        self._keras_inputs.append(ele)
        kt_id = str(id(ele))
        kt_index = i
        self._keras_inputs_ids_and_indices.append((kt_id, kt_index))

    # Wire up Node to Layers.
self.layer._inbound_nodes.append(self)
for kt in self.keras_inputs:
    inbound_layer = kt._keras_history.layer
    if inbound_layer is not None:  # `None` for `Input` tensors.
        inbound_layer._outbound_nodes.append(self)

    # Set metadata on outputs.
node_index = len(self.layer._inbound_nodes) - 1
for i, tensor in enumerate(nest.flatten(outputs)):
    tensor._keras_history = KerasHistory(
        layer=layer, node_index=node_index, tensor_index=i)

# Cached for performance.
self.flat_input_ids = [str(id(t)) for t in self._keras_inputs]
self.flat_output_ids = [str(id(t)) for t in nest.flatten(self.outputs)]
