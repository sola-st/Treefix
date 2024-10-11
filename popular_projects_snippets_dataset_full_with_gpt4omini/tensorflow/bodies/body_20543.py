# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding_test.py
"""Tests that frozen policies can't be changed."""
p1 = tpu_sharding.ShardingPolicy()
p1.freeze()
with self.assertRaises(ValueError):
    p1.set_number_of_shards(17)
with self.assertRaises(ValueError):
    p1.set_shard_dimension(22)
