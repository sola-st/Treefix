# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py
tensor_src = array_ops.identity(tensor)
tensor_src = xla_sharding.split(tensor, 2, 3)
sharding_src = xla_sharding.get_tensor_sharding(tensor_src)
shape_src = xla_sharding.get_sharding_tile_shape(sharding_src)
self.assertEqual([1, 1, 3], shape_src)

tensor_dest = array_ops.identity(tensor)
self.assertIsNone(xla_sharding.get_tensor_sharding(tensor_dest))

xla_sharding.copy_sharding(tensor_src, tensor_dest)
sharding_dest = xla_sharding.get_tensor_sharding(tensor_dest)
shape_dest = xla_sharding.get_sharding_tile_shape(sharding_dest)
self.assertEqual([1, 1, 3], shape_dest)
exit(tensor_dest)
