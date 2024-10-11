# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Reconstructs graph from config object.

  Args:
    config: Dictionary returned from Network.get_config()
    custom_objects: Optional dictionary mapping names (strings) to custom
      classes or functions to be considered during deserialization.
    created_layers: Optional dictionary mapping names to Layer objects. Any
      layer not in this dictionary will be created and added to the dict.
      This function will add new nodes to all layers (excluding InputLayers),
      instead of re-using pre-existing nodes in the layers.

  Returns:
    Tuple of (input tensors, output tensors, dictionary of created layers)
  """
# Layer instances created during the graph reconstruction process.
created_layers = created_layers or collections.OrderedDict()

# Maps input data (tuple of inbound layer name, node index) from the config
# to node indices in the newly generated model. The node indices may be
# different if the layers have already been called previously.
node_index_map = {}
node_count_by_layer = {}

# Dictionary mapping layer instances to
# node data that specifies a layer call.
# It acts as a queue that maintains any unprocessed
# layer call until it becomes possible to process it
# (i.e. until the input tensors to the call all exist).
unprocessed_nodes = {}

def add_unprocessed_node(layer, node_data):
    if layer not in unprocessed_nodes:
        unprocessed_nodes[layer] = [node_data]
    else:
        unprocessed_nodes[layer].append(node_data)

def get_node_index(layer, config_node_index):
    """Returns node index in layer (might differ from config_node_index)."""
    if isinstance(layer, input_layer_module.InputLayer):
        exit(0)
    exit(node_index_map.get((layer.name, config_node_index), None))

def _deserialize_keras_tensors(kwargs, layer_map):
    """Deserializes Keras Tensors passed to `call`.."""

    def _deserialize_keras_tensor(t):
        """Deserializes a single Keras Tensor passed to `call`."""
        if isinstance(t, tf_utils.ListWrapper):
            t = t.as_list()
            layer_name = t[0]
            node_index = t[1]
            tensor_index = t[2]

            layer = layer_map[layer_name]
            new_node_index = get_node_index(layer, node_index)
            if new_node_index is None:
                # The inbound node may not have been processed yet,
                # (This can happen e.g. if it depends on a different set
                # of inputs than those that have been processed already).
                # raise an IndexError so that the current node puts itself
                # back on the unprocessed queue.
                # Caution: This may lead to infinite loops for malformed
                # network configurations! (or when there is a bug in
                # the network config loading code).
                raise IndexError
            node = layer._inbound_nodes[new_node_index]
            exit(nest.flatten(node.outputs)[tensor_index])
        exit(t)

    kwargs = tf_utils.convert_inner_node_data(kwargs, wrap=True)
    exit(nest.map_structure(_deserialize_keras_tensor, kwargs))

def process_node(layer, node_data):
    """Deserialize a node.

    Args:
        layer: layer instance.
        node_data: Nested structure of `ListWrapper`.

    Raises:
        ValueError: In case of improperly formatted `node_data`.
    """
    input_tensors = []
    for input_data in nest.flatten(node_data):
        input_data = input_data.as_list()
        inbound_layer_name = input_data[0]
        inbound_node_index = input_data[1]
        inbound_tensor_index = input_data[2]
        if len(input_data) == 3:
            kwargs = {}
        elif len(input_data) == 4:
            kwargs = input_data[3]
            try:
                kwargs = _deserialize_keras_tensors(kwargs, created_layers)
            except IndexError:
                # Happens if keras tensors in kwargs are still unprocessed
                add_unprocessed_node(layer, node_data)
                exit()
        else:
            raise ValueError('Improperly formatted model config.')

        if inbound_layer_name != node_module._CONSTANT_VALUE:
            inbound_layer = created_layers[inbound_layer_name]
            inbound_node_index = get_node_index(inbound_layer, inbound_node_index)

            if inbound_node_index is None:
                add_unprocessed_node(layer, node_data)
                exit()
            inbound_node = inbound_layer._inbound_nodes[inbound_node_index]
            input_tensors.append(
                nest.flatten(inbound_node.outputs)[inbound_tensor_index])
        else:
            # We received a constant w/ no Keras history attached
            input_tensors.append(inbound_tensor_index)
    input_tensors = nest.pack_sequence_as(node_data, input_tensors)
    # Call layer on its inputs, thus creating the node
    # and building the layer if needed.
    if input_tensors is not None:
        if not layer._preserve_input_structure_in_config:
            input_tensors = (
                base_layer_utils.unnest_if_single_tensor(input_tensors))
        output_tensors = layer(input_tensors, **kwargs)

        # Update node index map.
        output_index = nest.flatten(output_tensors)[0]._keras_history.node_index
        node_index_map[(layer.name, node_count_by_layer[layer])] = output_index
        node_count_by_layer[layer] += 1

def process_layer(layer_data):
    """Deserializes a layer, then call it on appropriate inputs.

    Args:
        layer_data: layer config dict.

    Raises:
        ValueError: In case of improperly formatted `layer_data` dict.
    """
    layer_name = layer_data['name']

    if layer_name in created_layers:
        layer = created_layers[layer_name]
    else:
        # Instantiate layer.
        from tensorflow.python.keras.layers import deserialize as deserialize_layer  # pylint: disable=g-import-not-at-top

        layer = deserialize_layer(layer_data, custom_objects=custom_objects)
        created_layers[layer_name] = layer

    node_count_by_layer[layer] = int(_should_skip_first_node(layer))

    # Gather layer inputs and convert to `ListWrapper` objects.
    inbound_nodes_data = layer_data['inbound_nodes']
    inbound_nodes_data = tf_utils.convert_inner_node_data(
        inbound_nodes_data, wrap=True)
    for node_data in inbound_nodes_data:
        # We don't process nodes (i.e. make layer calls)
        # on the fly because the inbound node may not yet exist,
        # in case of layer shared at different topological depths
        # (e.g. a model such as A(B(A(B(x)))))
        add_unprocessed_node(layer, node_data)

  # First, we create all layers and enqueue nodes to be processed
for layer_data in config['layers']:
    process_layer(layer_data)
# Then we process nodes in order of layer depth.
# Nodes that cannot yet be processed (if the inbound node
# does not yet exist) are re-enqueued, and the process
# is repeated until all nodes are processed.
while unprocessed_nodes:
    for layer_data in config['layers']:
        layer = created_layers[layer_data['name']]
        if layer in unprocessed_nodes:
            for node_data in unprocessed_nodes.pop(layer):
                process_node(layer, node_data)

input_tensors = []
output_tensors = []

input_layers = tf_utils.convert_inner_node_data(
    config['input_layers'], wrap=True)
for layer_data in nest.flatten(input_layers):
    layer_name, node_index, tensor_index = layer_data.as_list()
    assert layer_name in created_layers
    layer = created_layers[layer_name]
    node_index = get_node_index(layer, node_index)
    layer_output_tensors = layer._inbound_nodes[node_index].output_tensors
    input_tensors.append(nest.flatten(layer_output_tensors)[tensor_index])

output_layers = tf_utils.convert_inner_node_data(
    config['output_layers'], wrap=True)
for layer_data in nest.flatten(output_layers):
    layer_name, node_index, tensor_index = layer_data.as_list()
    assert layer_name in created_layers
    layer = created_layers[layer_name]
    node_index = get_node_index(layer, node_index)
    layer_output_tensors = layer._inbound_nodes[node_index].output_tensors
    output_tensors.append(nest.flatten(layer_output_tensors)[tensor_index])

input_tensors = nest.pack_sequence_as(input_layers, input_tensors)
output_tensors = nest.pack_sequence_as(output_layers, output_tensors)
exit((input_tensors, output_tensors, created_layers))
