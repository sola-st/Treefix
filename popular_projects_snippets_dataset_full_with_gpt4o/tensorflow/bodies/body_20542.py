# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding_test.py
"""Tests that freezing a policy applies default values."""
p1 = tpu_sharding.ShardingPolicy()
p1.freeze()
self.assertEqual(p1.number_of_shards,
                 tpu_sharding._DEFAULT_NUMBER_OF_SHARDS)
self.assertEqual(p1.shard_dimension, tpu_sharding._DEFAULT_SHARD_DIMENSION)
p2 = tpu_sharding.ShardingPolicy()
p2.set_number_of_shards(17)
p2.set_shard_dimension(23)
p2.freeze()
self.assertEqual(p2.number_of_shards, 17)
self.assertEqual(p2.shard_dimension, 23)
