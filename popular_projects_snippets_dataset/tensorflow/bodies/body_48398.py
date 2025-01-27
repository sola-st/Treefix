# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
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
