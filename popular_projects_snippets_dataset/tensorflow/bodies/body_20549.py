# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding_test.py
"""Tests sharding and unsharding scalars."""
p = tpu_sharding.ShardingPolicy()
p.freeze()
self.assertEqual(p.get_sharded_shape([]), [])
self.assertEqual(p.get_unsharded_shape([[]]), [])
