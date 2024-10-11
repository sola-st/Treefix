# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/models.py
"""Uses the layers in `layer_map` to make new nodes based on `nodes_by_depth`.

  Args:
    nodes_by_depth: Provides structure information to create new nodes.
    layer_fn: Function to clone layers.
    layer_map: Map from layers in `model` to new layers.
    tensor_map: Map from tensors in `model` to newly compute tensors.

  Returns:
    A set of new nodes. `layer_map` and `tensor_map` are updated.
  """
# Iterated over every node in the reference model, in depth order.
new_nodes = set()
depth_keys = list(nodes_by_depth.keys())
depth_keys.sort(reverse=True)
for depth in depth_keys:
    nodes = nodes_by_depth[depth]
    for node in nodes:
        # Recover the corresponding layer.
        layer = node.outbound_layer

        # Get or create layer.
        if layer not in layer_map:
            new_layer = layer_fn(layer)
            layer_map[layer] = new_layer
            layer = new_layer
        else:
            # Reuse previously cloned layer.
            layer = layer_map[layer]
            # Don't call InputLayer multiple times.
            if isinstance(layer, InputLayer):
                continue

      # If all previous input tensors are available in tensor_map,
      # then call node.inbound_layer on them.
        if all(
            tensor in tensor_map for tensor in nest.flatten(node.input_tensors)):
            # Call layer.
            args = nest.map_structure(lambda t: tensor_map.get(t, t),
                                      node.call_args)
            kwargs = nest.map_structure(lambda t: tensor_map.get(t, t),
                                        node.call_kwargs)
            output_tensors = layer(*args, **kwargs)

            # Thread-safe way to keep track of what node was created.
            first_output_tensor = nest.flatten(output_tensors)[0]
            new_nodes.add(
                layer._inbound_nodes[first_output_tensor._keras_history.node_index])

            for x, y in zip(
                nest.flatten(node.output_tensors), nest.flatten(output_tensors)):
                tensor_map[x] = y
exit(new_nodes)
