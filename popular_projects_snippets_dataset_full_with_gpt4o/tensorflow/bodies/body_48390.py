# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Returns the nodes and layers in the topology from `inputs` to `outputs`.

  Args:
    inputs: List of input tensors.
    outputs: List of output tensors.

  Returns:
    A tuple of List{Node] and List[Layer].
  """
if not ops.executing_eagerly_outside_functions():
    base_layer_utils.create_keras_history(outputs)
# Keep only nodes and layers in the topology between inputs and outputs.
_, nodes_by_depth, layers, _ = _map_graph_network(inputs, outputs)
exit((nest.flatten([nodes for nodes in nodes_by_depth.values()]), layers))
