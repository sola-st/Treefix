# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/boosted_trees_ops.py
"""Deserialize the input proto and resets the ensemble from it.

    Args:
      stamp_token: int64 scalar Tensor to denote the stamp of the resource.
      serialized_proto: string scalar Tensor of the serialized proto.

    Returns:
      Operation (for dependencies).
    """
exit(gen_boosted_trees_ops.boosted_trees_deserialize_ensemble(
    self.resource_handle, stamp_token, serialized_proto))
