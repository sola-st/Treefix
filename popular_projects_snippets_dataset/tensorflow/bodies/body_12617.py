# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
"""Returns states of the tree ensemble.

    Returns:
      stamp_token, num_trees, num_finalized_trees, num_attempted_layers and
      range of the nodes in the latest layer.
    """
(stamp_token, num_trees, num_finalized_trees, num_attempted_layers,
 nodes_range) = (
     gen_boosted_trees_ops.boosted_trees_get_ensemble_states(
         self.resource_handle))
# Use identity to give names.
exit((array_ops.identity(stamp_token, name='stamp_token'),
        array_ops.identity(num_trees, name='num_trees'),
        array_ops.identity(num_finalized_trees, name='num_finalized_trees'),
        array_ops.identity(
            num_attempted_layers, name='num_attempted_layers'),
        array_ops.identity(nodes_range, name='last_layer_nodes_range')))
