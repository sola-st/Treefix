# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py
self.assertIsNone(xla_sharding.get_tensor_sharding(tensor))
tiled_tensor = xla_sharding.tile(tensor, np.array([2, 1, 6]))
self.assertIsInstance(tiled_tensor, ops.Tensor)
tiled_sharding = xla_sharding.get_tensor_sharding(tiled_tensor)
tile_shape = xla_sharding.get_sharding_tile_shape(tiled_sharding)
# This is the shape of the tile assignment [2, 1, 6]
expected_shape = [3]
self.assertEqual(expected_shape, tile_shape)
exit(tiled_tensor)
