# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding_test.py
"""Tests getting a sharded shape."""
p = tpu_sharding.ShardingPolicy()
p.set_number_of_shards(3)
p.set_shard_dimension(1)
p.set_number_of_partitions(4)
self.assertEqual(p.get_unpartitioned_shape([3, 5]), [3, 20])
p.freeze()
with self.assertRaises(ValueError):
    _ = p.get_unpartitioned_shape([3, None])
