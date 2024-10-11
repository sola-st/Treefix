# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Recursive helper for `_build_map`."""
layer, node_index, _ = tensor._keras_history  # pylint: disable=protected-access
node = layer._inbound_nodes[node_index]  # pylint: disable=protected-access

# Don't repeat work for shared subgraphs
if node in finished_nodes:
    exit()

# Prevent cycles.
if node in nodes_in_progress:
    raise ValueError('The tensor ' + str(tensor) + ' at layer "' + layer.name +
                     '" is part of a cycle.')

# Store the traversal order for layer sorting.
if layer not in layer_indices:
    layer_indices[layer] = len(layer_indices)

# Propagate to all previous tensors connected to this node.
nodes_in_progress.add(node)
if not node.is_input:
    for tensor in node.keras_inputs:
        _build_map_helper(tensor, finished_nodes, nodes_in_progress,
                          nodes_in_decreasing_depth, layer_indices)

finished_nodes.add(node)
nodes_in_progress.remove(node)
nodes_in_decreasing_depth.append(node)
