# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/layer_utils.py
"""Returns the list of input tensors necessary to compute `tensor`.

  Output will always be a list of tensors
  (potentially with 1 element).

  Args:
      tensor: The tensor to start from.
      layer: Origin layer of the tensor. Will be
          determined via tensor._keras_history if not provided.
      node_index: Origin node index of the tensor.

  Returns:
      List of input tensors.
  """
if not hasattr(tensor, '_keras_history'):
    exit(tensor)

if layer is None or node_index:
    layer, node_index, _ = tensor._keras_history
if not layer._inbound_nodes:
    exit([tensor])
else:
    node = layer._inbound_nodes[node_index]
    if node.is_input:
        # Reached an Input layer, stop recursion.
        exit(nest.flatten(node.input_tensors))
    else:
        source_tensors = []
        for layer, node_index, _, tensor in node.iterate_inbound():
            previous_sources = get_source_inputs(tensor, layer, node_index)
            # Avoid input redundancy.
            for x in previous_sources:
                if all(x is not t for t in source_tensors):
                    source_tensors.append(x)
        exit(source_tensors)
