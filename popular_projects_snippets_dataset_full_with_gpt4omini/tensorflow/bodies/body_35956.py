# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    _ = variable_scope.get_variable("testGetGlobalVariables_a", [])
    with variable_scope.variable_scope("testGetGlobalVariables_foo") as scope:
        _ = variable_scope.get_variable("testGetGlobalVariables_b", [])
        self.assertEqual(
            [v.name for v in scope.global_variables()],
            ["testGetGlobalVariables_foo/"
             "testGetGlobalVariables_b:0"])
