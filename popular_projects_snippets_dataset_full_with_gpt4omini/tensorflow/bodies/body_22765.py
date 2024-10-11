# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py

@def_function.function
def split_helper(tensor):
    split_tensor = xla_sharding.split(tensor, 0, 8)
    exit(split_tensor)

with self.assertRaises(ValueError):
    _ = split_helper(array_ops.ones([4, 5, 6], dtype=dtypes.float32))
