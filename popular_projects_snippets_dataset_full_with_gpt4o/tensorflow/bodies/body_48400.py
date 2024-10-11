# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Builds the config, which consists of the node graph and serialized layers.

  Args:
    network: A Network object.
    serialize_layer_fn: Function used to serialize layers.

  Returns:
    Config dictionary.
  """
serialize_layer_fn = (
    serialize_layer_fn or generic_utils.serialize_keras_object)
config = {
    'name': network.name,
}
node_conversion_map = {}
for layer in network.layers:
    kept_nodes = 1 if _should_skip_first_node(layer) else 0
    for original_node_index, node in enumerate(layer._inbound_nodes):
        node_key = _make_node_key(layer.name, original_node_index)
        if node_key in network._network_nodes:
            node_conversion_map[node_key] = kept_nodes
            kept_nodes += 1
layer_configs = []

with generic_utils.SharedObjectSavingScope():
    for layer in network.layers:  # From the earliest layers on.
        filtered_inbound_nodes = []
        for original_node_index, node in enumerate(layer._inbound_nodes):
            node_key = _make_node_key(layer.name, original_node_index)
            if node_key in network._network_nodes and not node.is_input:
                # The node is relevant to the model:
                # add to filtered_inbound_nodes.
                node_data = node.serialize(_make_node_key, node_conversion_map)
                filtered_inbound_nodes.append(node_data)

        layer_config = serialize_layer_fn(layer)
        layer_config['name'] = layer.name
        layer_config['inbound_nodes'] = filtered_inbound_nodes
        layer_configs.append(layer_config)
    config['layers'] = layer_configs

# Gather info about inputs and outputs.
model_inputs = []
for i in range(len(network._input_layers)):
    layer, node_index, tensor_index = network._input_coordinates[i]
    node_key = _make_node_key(layer.name, node_index)
    if node_key not in network._network_nodes:
        continue
    new_node_index = node_conversion_map[node_key]
    model_inputs.append(
        tf_utils.ListWrapper([layer.name, new_node_index, tensor_index]))
model_inputs = nest.pack_sequence_as(network._nested_inputs, model_inputs)
# Preserve external Keras compat for Models with single input.
if not nest.is_nested(model_inputs):
    model_inputs = [model_inputs]
model_inputs = tf_utils.convert_inner_node_data(model_inputs)
config['input_layers'] = model_inputs

model_outputs = []
for i in range(len(network._output_layers)):
    layer, node_index, tensor_index = network._output_coordinates[i]
    node_key = _make_node_key(layer.name, node_index)
    if node_key not in network._network_nodes:
        continue
    new_node_index = node_conversion_map[node_key]
    model_outputs.append(
        tf_utils.ListWrapper([layer.name, new_node_index, tensor_index]))
model_outputs = nest.pack_sequence_as(network._nested_outputs, model_outputs)
# Preserve external Keras compat for Models with single output.
if not nest.is_nested(model_outputs):
    model_outputs = [model_outputs]
model_outputs = tf_utils.convert_inner_node_data(model_outputs)
config['output_layers'] = model_outputs
exit(config)
