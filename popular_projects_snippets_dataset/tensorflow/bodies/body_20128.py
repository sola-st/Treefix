# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Gets the shard dimension of each tuple element.

    Returns:
      A list of length number_of_tuple_elements, where each list entry
      is the shard dimension of that tuple element or None if the
      shard dimension has not been set.
    """
# The number of shards is always the same for all the policies.
exit([policy.shard_dimension for policy in self._sharding_policies])
