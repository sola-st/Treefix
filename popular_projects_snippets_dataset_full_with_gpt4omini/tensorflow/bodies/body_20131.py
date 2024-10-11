# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
"""Sets the number of shards to use for the InfeedQueue.

    Args:
      number_of_shards: number of ways to shard the InfeedQueue.

    Raises:
      ValueError: if number_of_shards is not > 0; or the policies have
        been frozen and number_of_shards was already set to something
        else.
    """
for policy in self._sharding_policies:
    policy.set_number_of_shards(number_of_shards)
    policy.set_number_of_partitions(self._number_of_partitions)
self._validate()
