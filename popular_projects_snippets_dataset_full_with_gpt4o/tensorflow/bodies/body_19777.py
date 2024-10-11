# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_infeed_test.py
"""Tests that the constructor can be called with different arguments."""
i = tpu_feed.InfeedQueue(number_of_tuple_elements=2)
self.assertEqual(i.number_of_tuple_elements, 2)
self.assertEqual(i.tuple_types, None)
self.assertEqual(i.tuple_shapes, None)
self.assertEqual(i.number_of_shards, None)
i = tpu_feed.InfeedQueue(
    tuple_types=[dtypes.float32, dtypes.int32, dtypes.int32])
self.assertEqual(i.number_of_tuple_elements, 3)
self.assertEqual(i.tuple_types,
                 [dtypes.float32, dtypes.int32, dtypes.int32])
self.assertEqual(i.tuple_shapes, None)
self.assertEqual(i.number_of_shards, None)
i = tpu_feed.InfeedQueue(tuple_shapes=[[1], [2, 3]])
self.assertEqual(i.number_of_tuple_elements, 2)
self.assertEqual(i.tuple_types, None)
self.assertEqual(i.tuple_shapes, [[1], [2, 3]])
self.assertEqual(i.number_of_shards, None)
i = tpu_feed.InfeedQueue(shard_dimensions=[1, 0, 7])
self.assertEqual(i.number_of_tuple_elements, 3)
self.assertEqual(i.tuple_types, None)
self.assertEqual(i.tuple_shapes, None)
self.assertEqual([p.shard_dimension
                  for p in i.sharding_policies], [1, 0, 7])
with self.assertRaises(ValueError):
    i = tpu_feed.InfeedQueue()
with self.assertRaises(ValueError):
    i = tpu_feed.InfeedQueue(
        number_of_tuple_elements=2, tuple_types=[dtypes.float32])
with self.assertRaises(ValueError):
    i = tpu_feed.InfeedQueue(number_of_tuple_elements=2, tuple_shapes=[[1]])
with self.assertRaises(ValueError):
    i = tpu_feed.InfeedQueue(number_of_tuple_elements=2, shard_dimensions=[1])
with self.assertRaises(ValueError):
    i = tpu_feed.InfeedQueue(tuple_shapes=[[1], [2, 3]], shard_dimensions=[1])
