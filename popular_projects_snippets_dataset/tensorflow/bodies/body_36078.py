# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(initial_value=lambda: 1,
                                           name="var2")
self.assertEqual(dtypes.int32, v.value().dtype)
