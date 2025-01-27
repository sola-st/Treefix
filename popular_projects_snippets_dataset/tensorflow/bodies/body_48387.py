# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Validates a network's topology and gather its layers and nodes.

  Args:
    inputs: List of input tensors.
    outputs: List of outputs tensors.

  Returns:
    A tuple `(nodes, nodes_by_depth, layers, layers_by_depth)`.
    - nodes: list of Node instances.
    - nodes_by_depth: dict mapping ints (depth) to lists of node instances.
    - layers: list of Layer instances.
    - layers_by_depth: dict mapping ints (depth) to lists of layer instances.

  Raises:
    ValueError: In case the network is not valid (e.g. disconnected graph).
  """
# "depth" is number of layers between output Node and the Node.
# Nodes are ordered from inputs -> outputs.
nodes_in_decreasing_depth, layer_indices = _build_map(outputs)
network_nodes = {
    _make_node_key(node.layer.name, node.layer._inbound_nodes.index(node))
    for node in nodes_in_decreasing_depth
}

nodes_depths = {}  # dict {node: depth value}
layers_depths = {}  # dict {layer: depth value}

for node in reversed(nodes_in_decreasing_depth):
    # If the depth is not set, the node has no outbound nodes (depth 0).
    depth = nodes_depths.setdefault(node, 0)

    # Update the depth of the corresponding layer
    previous_depth = layers_depths.get(node.layer, 0)
    # If we've seen this layer before at a higher depth,
    # we should use that depth instead of the node depth.
    # This is necessary for shared layers that have inputs at different
    # depth levels in the graph.
    depth = max(depth, previous_depth)
    layers_depths[node.layer] = depth
    nodes_depths[node] = depth

    # Update the depth of inbound nodes.
    # The "depth" of a node is the max of the depths
    # of all nodes it is connected to + 1.
    for node_dep in node.parent_nodes:
        previous_depth = nodes_depths.get(node_dep, 0)
        nodes_depths[node_dep] = max(depth + 1, previous_depth)

  # Handle inputs that are not connected to outputs.
  # We do not error out here because the inputs may be used to compute losses
  # and metrics.
for input_t in inputs:
    input_layer = input_t._keras_history[0]
    if input_layer not in layers_depths:
        layers_depths[input_layer] = 0
        layer_indices[input_layer] = -1
        nodes_depths[input_layer._inbound_nodes[0]] = 0
        network_nodes.add(_make_node_key(input_layer.name, 0))

  # Build a dict {depth: list of nodes with this depth}
nodes_by_depth = collections.defaultdict(list)
for node, depth in nodes_depths.items():
    nodes_by_depth[depth].append(node)

# Build a dict {depth: list of layers with this depth}
layers_by_depth = collections.defaultdict(list)
for layer, depth in layers_depths.items():
    layers_by_depth[depth].append(layer)

# Get sorted list of layer depths.
depth_keys = list(layers_by_depth.keys())
depth_keys.sort(reverse=True)

# Set self.layers ordered by depth.
layers = []
for depth in depth_keys:
    layers_for_depth = layers_by_depth[depth]
    # Network.layers needs to have a deterministic order:
    # here we order them by traversal order.
    layers_for_depth.sort(key=lambda x: layer_indices[x])
    layers.extend(layers_for_depth)

# Get sorted list of node depths.
depth_keys = list(nodes_by_depth.keys())
depth_keys.sort(reverse=True)

# Check that all tensors required are computable.
# computable_tensors: all tensors in the graph
# that can be computed from the inputs provided.
computable_tensors = set()
for x in inputs:
    computable_tensors.add(id(x))

layers_with_complete_input = []  # To provide a better error msg.
for depth in depth_keys:
    for node in nodes_by_depth[depth]:
        layer = node.layer
        if layer and not node.is_input:
            for x in nest.flatten(node.keras_inputs):
                if id(x) not in computable_tensors:
                    raise ValueError('Graph disconnected: '
                                     'cannot obtain value for tensor ' + str(x) +
                                     ' at layer "' + layer.name + '". '
                                     'The following previous layers '
                                     'were accessed without issue: ' +
                                     str(layers_with_complete_input))
            for x in nest.flatten(node.outputs):
                computable_tensors.add(id(x))
            layers_with_complete_input.append(layer.name)

  # Ensure name unicity, which will be crucial for serialization
  # (since serialized nodes refer to layers by their name).
all_names = [layer.name for layer in layers]
for name in all_names:
    if all_names.count(name) != 1:
        raise ValueError('The name "' + name + '" is used ' +
                         str(all_names.count(name)) + ' times in the model. '
                         'All layer names should be unique.')
exit((network_nodes, nodes_by_depth, layers, layers_by_depth))
