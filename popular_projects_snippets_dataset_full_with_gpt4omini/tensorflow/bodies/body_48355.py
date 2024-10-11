# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
# This method is needed for Sequential to reinitialize graph network when
# layer is added or removed.
self._is_graph_network = True

# Normalize and set self.inputs, self.outputs.
if isinstance(inputs, list) and len(nest.flatten(inputs)) == 1:
    inputs = inputs[0]
if isinstance(outputs, list) and len(nest.flatten(outputs)) == 1:
    outputs = outputs[0]
self._nested_inputs = inputs
self._nested_outputs = outputs
self.inputs = nest.flatten(inputs)
self.outputs = nest.flatten(outputs)

# Models constructed with a single Tensor or list of Tensors can
# be called with a dict, where the keys of the dict are the names
# of the `Input` objects. Extra keys are ignored with warning.
if not nest.is_nested(self._nested_inputs):
    self._enable_dict_to_input_mapping = True
elif (isinstance(self._nested_inputs, (list, tuple)) and
      not any(nest.is_nested(t) for t in self._nested_inputs)):
    self._enable_dict_to_input_mapping = True
elif (isinstance(self._nested_inputs, dict) and
      not any(nest.is_nested(t) for t in self._nested_inputs.values())):
    self._enable_dict_to_input_mapping = True
else:
    self._enable_dict_to_input_mapping = False

if not ops.executing_eagerly_outside_functions():
    if any(not hasattr(tensor, '_keras_history') for tensor in self.outputs):
        base_layer_utils.create_keras_history(self._nested_outputs)

self._validate_graph_inputs_and_outputs()

# A Network does not create weights of its own, thus it is already
# built.
self.built = True
self._build_input_shape = nest.map_structure(lambda x: x.shape, inputs)
self._compute_output_and_mask_jointly = True
# `_expects_training_arg` is True since the `training` argument is always
# present in the signature of the `call` method of a graph network.
self._expects_training_arg = True
self._expects_mask_arg = True
# A graph network does not autocast inputs, as its layers will cast them
# instead.
self._autocast = False

self._input_layers = []
self._output_layers = []
self._input_coordinates = []
self._output_coordinates = []

# This is for performance optimization when calling the Network on new
# inputs. Every time the Network is called on a set on input tensors,
# we compute the output tensors, output masks and output shapes in one pass,
# then cache them here. When any of these outputs is queried later, we
# retrieve it from there instead of recomputing it.
self._output_mask_cache = {}
self._output_tensor_cache = {}
self._output_shape_cache = {}

# Build self._output_layers:
for x in self.outputs:
    layer, node_index, tensor_index = x._keras_history  # pylint: disable=protected-access
    self._output_layers.append(layer)
    self._output_coordinates.append((layer, node_index, tensor_index))

# Build self._input_layers:
for x in self.inputs:
    layer, node_index, tensor_index = x._keras_history  # pylint: disable=protected-access
    # It's supposed to be an input layer, so only one node
    # and one tensor output.
    assert node_index == 0
    assert tensor_index == 0
    self._input_layers.append(layer)
    self._input_coordinates.append((layer, node_index, tensor_index))

# Keep track of the network's nodes and layers.
nodes, nodes_by_depth, layers, _ = _map_graph_network(
    self.inputs, self.outputs)
self._network_nodes = nodes
self._nodes_by_depth = nodes_by_depth
self._self_tracked_trackables = layers
self._layer_call_argspecs = {}
for layer in self._self_tracked_trackables:
    self._layer_call_argspecs[layer] = tf_inspect.getfullargspec(layer.call)

# Build self.input_names and self.output_names.
self._set_output_names()
self.input_names = []
self._feed_input_names = []
self._feed_inputs = []
self._feed_input_shapes = []
for layer in self._input_layers:
    self.input_names.append(layer.name)
    if layer.is_placeholder:
        self._feed_input_names.append(layer.name)
        # Use batch_input_shape here because non-eager composite tensors may not
        # have a shape attribute that's meaningful (sparse, for instance, has
        # a tensor that's non-constant and needs to be fed). This means that
        # input layers that create placeholders will need to have the
        # batch_input_shape attr to allow for input shape validation.
        self._feed_input_shapes.append(layer._batch_input_shape)
        self._feed_inputs.append(layer.input)

self._compute_tensor_usage_count()
self._set_save_spec(self._nested_inputs)
tf_utils.assert_no_legacy_layers(self.layers)
