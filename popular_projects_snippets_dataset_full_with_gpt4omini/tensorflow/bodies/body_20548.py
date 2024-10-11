# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding_test.py
"""Tests getting an unsharded shape."""
p = tpu_sharding.ShardingPolicy()
p.set_number_of_shards(2)
p.set_shard_dimension(1)
self.assertEqual(p.get_unsharded_shape([[4, 3], [4, 3]]), [4, 6])
with self.assertRaises(ValueError):
    _ = p.get_unsharded_shape([[4, 3]])
with self.assertRaises(ValueError):
    _ = p.get_unsharded_shape([[4, 3], [4, 3], [4, 3]])
with self.assertRaises(ValueError):
    _ = p.get_unsharded_shape([[4, 3], [4, 2]])
with self.assertRaises(TypeError):
    _ = p.get_unsharded_shape([[4, 3], "not_a_shape"])
with self.assertRaises(ValueError):
    _ = p.get_unsharded_shape([None, [4, 3]])
with self.assertRaises(ValueError):
    _ = p.get_unsharded_shape([[2], [4, 3]])
