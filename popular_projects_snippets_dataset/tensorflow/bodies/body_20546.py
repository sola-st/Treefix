# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding_test.py
"""Tests getting a sharded shape."""
p = tpu_sharding.ShardingPolicy()
p.set_number_of_shards(3)
p.set_shard_dimension(1)
self.assertEqual(p.get_sharded_shape([4, 9]), [4, 3])
p.freeze()
with self.assertRaises(ValueError):
    p.set_shard_dimension(0)
with self.assertRaises(ValueError):
    _ = p.get_sharded_shape([4, 9], shard_index=4)
with self.assertRaises(ValueError):
    _ = p.get_sharded_shape([4, 9], shard_index=-1)
with self.assertRaises(TypeError):
    _ = p.get_sharded_shape("not_a_shape")
with self.assertRaises(ValueError):
    _ = p.get_sharded_shape(tensor_shape.TensorShape(None))
with self.assertRaises(ValueError):
    _ = p.get_sharded_shape([4, 10], shard_index=-1)
