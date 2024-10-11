# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with graph.as_default():
    with variable_scope.variable_scope("foo"):
        if i == 0:
            v = variable_scope.get_variable("v", [])
            self.assertEqual("foo/v:0", v.name)
        else:
            # Any thread after the first one should fail to create variable
            # with the same name.
            with self.assertRaises(ValueError):
                variable_scope.get_variable("v", [])
