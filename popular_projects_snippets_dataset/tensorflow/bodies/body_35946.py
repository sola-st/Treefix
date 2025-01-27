# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    root_scope = variable_scope.get_variable_scope()
    with variable_scope.variable_scope(
        root_scope, auxiliary_name_scope=False) as scope:
        self.assertEqual(scope.original_name_scope, "")
        self.assertEqual(variable_scope.get_variable("w", []).name, "w:0")
        self.assertEqual(constant_op.constant([], name="c").name, "c:0")

    with variable_scope.variable_scope("outer"):
        with variable_scope.variable_scope(
            root_scope, auxiliary_name_scope=False) as inner:
            self.assertEqual(inner.original_name_scope, "")
            self.assertEqual(variable_scope.get_variable("w1", []).name, "w1:0")
            self.assertEqual(
                constant_op.constant([], name="c1").name, "outer/c1:0")
