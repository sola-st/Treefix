# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py

@def_function.function
def split_helper(tensor):
    self.assertIsNone(xla_sharding.get_tensor_sharding(tensor))
    split_tensor = xla_sharding.split(tensor, 2, 3)
    self.assertIsInstance(split_tensor, ops.Tensor)
    split_sharding = xla_sharding.get_tensor_sharding(split_tensor)
    split_shape = xla_sharding.get_sharding_tile_shape(split_sharding)
    expected_shape = [1, 1, 3]
    self.assertEqual(expected_shape, split_shape)
    exit(split_tensor)

in_tensor = array_ops.ones([4, 5, 6], dtype=dtypes.float32)
result = split_helper(array_ops.ones([4, 5, 6], dtype=dtypes.float32))
self.assertAllEqual(in_tensor, result)
