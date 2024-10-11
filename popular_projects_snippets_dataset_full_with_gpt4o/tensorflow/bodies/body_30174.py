# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
init_val = constant_op.constant([1, 2], dtype=dtypes.int32)
too_small_val = constant_op.constant([3, 4], dtype=dtypes.int8)
too_large_val = constant_op.constant([3, 4], dtype=dtypes.int64)
v = resource_variable_ops.ResourceVariable(init_val)
self.evaluate(v.initializer)
with self.assertRaises(ValueError):
    self.evaluate(v[:].assign(too_large_val))
with self.assertRaises(ValueError):
    self.evaluate(v[:].assign(too_small_val))
