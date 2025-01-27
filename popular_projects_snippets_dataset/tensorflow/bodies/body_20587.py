# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding.py
"""Merges the policy of another policy into the current policy.

    Args:
      other: The policy to merge into this one.

    Raises:
      ValueError: If this policy has been frozen and the merge conflicts with
      the frozen policy.
    """
if other.number_of_shards is not None:
    self.set_number_of_shards(other.number_of_shards)
if other.shard_dimension is not None:
    self.set_shard_dimension(other.shard_dimension)
