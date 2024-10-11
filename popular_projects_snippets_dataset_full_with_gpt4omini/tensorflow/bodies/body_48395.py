# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
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
