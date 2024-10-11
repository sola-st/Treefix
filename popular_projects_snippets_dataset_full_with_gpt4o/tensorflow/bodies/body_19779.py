# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_infeed_test.py
"""Tests freezing the queue."""
i = tpu_feed.InfeedQueue(number_of_tuple_elements=2)
t1 = constant_op.constant(1, dtypes.int32, shape=[2])
t2 = constant_op.constant(2.0, dtypes.float32, shape=[2, 4])
i.set_configuration_from_sharded_input_tensors([[t2, t1], [t2, t1]])
self.assertEqual(i.number_of_shards, 2)
self.assertEqual(i.tuple_shapes, [[4, 4], [4]])
self.assertEqual(i.tuple_types, [dtypes.float32, dtypes.int32])
self.assertEqual(i.shard_dimensions, [0, 0])
i.freeze()
i.set_number_of_shards(2)
i.set_tuple_shapes([[4, 4], [4]])
i.set_tuple_types([dtypes.float32, dtypes.int32])
i.set_shard_dimensions([0, 0])
with self.assertRaises(ValueError):
    i.set_number_of_shards(1)
with self.assertRaises(ValueError):
    i.set_tuple_shapes([[8, 8], [8]])
with self.assertRaises(ValueError):
    i.set_tuple_types([dtypes.int32, dtypes.float32])
with self.assertRaises(ValueError):
    i.set_shard_dimensions([1, 0])
self.assertEqual(i.number_of_shards, 2)
self.assertEqual(i.tuple_shapes, [[4, 4], [4]])
self.assertEqual(i.tuple_types, [dtypes.float32, dtypes.int32])
self.assertEqual(i.shard_dimensions, [0, 0])
