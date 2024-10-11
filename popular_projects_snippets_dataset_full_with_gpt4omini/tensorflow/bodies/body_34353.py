# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
m = map_ops.empty_tensor_map()
with self.assertRaisesRegex(
    errors.InvalidArgumentError, "TensorMapStackKeys cannot be called "
    "on empty map."):
    keys = map_ops.tensor_map_stack_keys(m, dtypes.float32)
    self.evaluate(keys)
