# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding_test.py
"""Tests the string representation."""
p1 = tpu_sharding.ShardingPolicy()
self.assertEqual(str(p1), "ShardingPolicy(unset)")
p1.set_number_of_shards(17)
self.assertEqual(str(p1), "ShardingPolicy(unset)")
p1.set_shard_dimension(8)
self.assertEqual(str(p1), "ShardingPolicy(17 shards dimension 8)")
