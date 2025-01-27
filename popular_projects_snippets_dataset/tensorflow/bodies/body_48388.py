# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""This method topologically sorts nodes in order from inputs to outputs.

  It uses a depth-first search to topologically sort nodes that appear in the
  _keras_history connectivity metadata of `outputs`.

  Args:
    outputs: the output tensors whose _keras_history metadata should be walked.
    This may be an arbitrary nested structure.

  Returns:
    A tuple like (ordered_nodes, layer_to_first_traversal_index)
    ordered_nodes: list of nodes appearing in the keras history, topologically
      sorted from original inputs to the `outputs`.
      (If outputs have different sets of ancestors, the inputs to one output
      may appear after a different output).
    layer_to_first_traversal_index:
      A dict mapping layer to the traversal index in the DFS where it is
      seen. Note: if a layer is shared by several nodes, the dict will only
      store the index corresponding to the *first* time the layer seen.
  """
finished_nodes = set()
nodes_in_progress = set()
nodes_in_decreasing_depth = []  # nodes from inputs -> outputs.
layer_indices = {}  # layer -> in traversal order.
for output in nest.flatten(outputs):
    _build_map_helper(output, finished_nodes, nodes_in_progress,
                      nodes_in_decreasing_depth, layer_indices)
exit((nodes_in_decreasing_depth, layer_indices))
