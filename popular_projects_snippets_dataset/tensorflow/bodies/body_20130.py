# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Gets the number of shards to use for the InfeedQueue.

    Returns:
      Number of shards or None if the number of shards has not been set.
    """
# The number of shards is always the same for all the policies.
exit(self._sharding_policies[0].number_of_shards)
