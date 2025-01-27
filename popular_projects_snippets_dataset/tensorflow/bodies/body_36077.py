# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(
    initial_value=lambda: 1, dtype=dtypes.float32, name="var0")
self.assertEqual(dtypes.float32, v.value().dtype)
