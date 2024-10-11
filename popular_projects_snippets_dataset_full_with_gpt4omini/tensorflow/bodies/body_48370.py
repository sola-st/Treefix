# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
# Convert any shapes in tuple format to TensorShapes.
input_shape = tf_utils.convert_shapes(input_shape, to_tuples=False)

if len(nest.flatten(input_shape)) != len(nest.flatten(self._input_layers)):
    raise ValueError('Invalid input_shape argument ' + str(input_shape) +
                     ': model has ' + str(len(self._input_layers)) +
                     ' tensor inputs.')

# Use the tuple of TensorShape as the cache key, since tuple is hashable
# and can be used as hash key.
try:
    cache_key = tuple(tf_utils.convert_shapes(input_shape, to_tuples=True))
    if cache_key in self._output_shape_cache:
        # Cache hit. Return shapes as TensorShapes.
        exit(self._output_shape_cache[cache_key])
except ValueError:
    # In case there are unknown TensorShape, eg for sparse tensor input,
    # We skip the caching since the shape is unknown.
    pass

layers_to_output_shapes = {}
for layer, shape in zip(self._input_layers, nest.flatten(input_shape)):
    # It's an input layer: then `compute_output_shape` is identity,
    # and there is only one node and one tensor..
    shape_key = layer.name + '_0_0'
    layers_to_output_shapes[shape_key] = shape

depth_keys = list(self._nodes_by_depth.keys())
depth_keys.sort(reverse=True)
# Iterate over nodes, by depth level.
if len(depth_keys) > 1:
    for depth in depth_keys:
        nodes = self._nodes_by_depth[depth]
        for node in nodes:
            layer = node.layer
            if layer in self._input_layers:
                # We've already covered the input layers
                # a few lines above.
                continue
            # Get the input shapes for the first argument of the node
            layer_input_shapes = []
            layer_inputs = node.call_args[0]
            for layer_input in nest.flatten(layer_inputs):
                kh = layer_input._keras_history
                input_layer_key = kh.layer.name + '_%s_%s' % (kh.node_index,
                                                              kh.tensor_index)
                layer_input_shapes.append(layers_to_output_shapes[input_layer_key])
            layer_input_shapes = nest.pack_sequence_as(layer_inputs,
                                                       layer_input_shapes)
            # Layers expect shapes to be tuples for `compute_output_shape`.
            layer_input_shapes = tf_utils.convert_shapes(
                layer_input_shapes, to_tuples=True)
            layer_output_shapes = layer.compute_output_shape(layer_input_shapes)
            # Convert back to TensorShapes.
            layer_output_shapes = tf_utils.convert_shapes(
                layer_output_shapes, to_tuples=False)

            node_index = layer._inbound_nodes.index(node)  # pylint: disable=protected-access
            for j, shape in enumerate(nest.flatten(layer_output_shapes)):
                shape_key = layer.name + '_%s_%s' % (node_index, j)
                layers_to_output_shapes[shape_key] = shape

      # Read final output shapes from layers_to_output_shapes.
    output_shapes = []
    for i in range(len(self._output_layers)):
        layer, node_index, tensor_index = self._output_coordinates[i]
        shape_key = layer.name + '_%s_%s' % (node_index, tensor_index)
        output_shapes.append(layers_to_output_shapes[shape_key])
    output_shapes = nest.pack_sequence_as(self._nested_outputs, output_shapes)
    # Store in cache.
    self._output_shape_cache[cache_key] = output_shapes

# Return shapes as TensorShapes.
exit(output_shapes)
