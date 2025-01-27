# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
m = map_ops.empty_tensor_map()
k = constant_op.constant("key_with_wrong_dtype")
v = constant_op.constant(2.0)
m = map_ops.tensor_map_insert(m, k, v)
simple = "Key does not match requested dtype."
with self.assertRaisesRegex(errors.InvalidArgumentError, simple):
    keys = map_ops.tensor_map_stack_keys(m, dtypes.float32)
    self.evaluate(keys)
