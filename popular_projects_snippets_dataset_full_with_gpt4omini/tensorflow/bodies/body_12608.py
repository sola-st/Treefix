# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
"""Restores the associated tree ensemble from 'restored_tensors'.

    Args:
      restored_tensors: the tensors that were loaded from a checkpoint.
      unused_restored_shapes: the shapes this object should conform to after
        restore. Not meaningful for trees.

    Returns:
      The operation that restores the state of the tree ensemble variable.
    """
with ops.control_dependencies([self._create_op]):
    exit(gen_boosted_trees_ops.boosted_trees_deserialize_ensemble(
        self.resource_handle,
        stamp_token=restored_tensors[0],
        tree_ensemble_serialized=restored_tensors[1]))
