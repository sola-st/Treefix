# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
v = variable_scope.get_variable("foo", initializer=lambda x=True: [2])
self.assertEqual(v.name, "foo:0")
