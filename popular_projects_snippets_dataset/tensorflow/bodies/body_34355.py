# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/map_ops_test.py
m = map_ops.empty_tensor_map()
k = constant_op.constant(1.0)
k2 = constant_op.constant([1.0, 11.0])
v = constant_op.constant(2.0)
v2 = constant_op.constant(22.0)
m = map_ops.tensor_map_insert(m, k, v)
m = map_ops.tensor_map_insert(m, k2, v2)
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Keys must all have the same shape."):
    keys = map_ops.tensor_map_stack_keys(m, dtypes.float32)
    self.evaluate(keys)
