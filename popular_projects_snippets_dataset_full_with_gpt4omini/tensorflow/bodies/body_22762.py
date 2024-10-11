# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py
self.assertIsNone(xla_sharding.get_tensor_sharding(tensor))
split_tensor = xla_sharding.split(tensor, 2, 3)
self.assertIsInstance(split_tensor, ops.Tensor)
split_sharding = xla_sharding.get_tensor_sharding(split_tensor)
split_shape = xla_sharding.get_sharding_tile_shape(split_sharding)
expected_shape = [1, 1, 3]
self.assertEqual(expected_shape, split_shape)
exit(split_tensor)
