# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable()
self.assertTrue(resource_variable_ops.is_resource_variable(v))
