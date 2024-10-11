# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
vs = variable_scope._get_default_variable_store()
v = vs.get_variable("v", [1])
v1 = vs.get_variable("v", [1])
self.assertIs(v, v1)
