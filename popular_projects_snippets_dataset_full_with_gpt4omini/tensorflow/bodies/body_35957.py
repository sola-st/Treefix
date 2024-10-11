# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    _ = variable_scope.get_variable(
        "a", [], collections=[ops.GraphKeys.LOCAL_VARIABLES])
    with variable_scope.variable_scope("foo") as scope:
        _ = variable_scope.get_variable(
            "b", [], collections=[ops.GraphKeys.LOCAL_VARIABLES])
        _ = variable_scope.get_variable("c", [])
        self.assertEqual([v.name for v in scope.local_variables()], ["foo/b:0"])
