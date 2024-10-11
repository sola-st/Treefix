# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py

@def_function.function
def replicate_helper(tensor):
    replicated_tensor = xla_sharding.replicate(
        array_ops.ones([4, 5, 6], dtype=dtypes.float32))
    self.assertIsNone(xla_sharding.get_tensor_sharding(tensor))
    replicated_sharding = xla_sharding.get_tensor_sharding(replicated_tensor)
    self.assertIsNotNone(replicated_sharding)
    self.assertIsNone(
        xla_sharding.get_sharding_tile_shape(replicated_sharding))
    exit(replicated_tensor)

in_tensor = array_ops.ones([4, 5, 6], dtype=dtypes.float32)
result = replicate_helper(array_ops.ones([4, 5, 6], dtype=dtypes.float32))
self.assertAllEqual(in_tensor, result)
