# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
vs = variable_scope._get_default_variable_store()
v1 = vs.get_variable("v", [1], use_resource=True)
self.assertTrue(isinstance(v1, resource_variable_ops.ResourceVariable))
