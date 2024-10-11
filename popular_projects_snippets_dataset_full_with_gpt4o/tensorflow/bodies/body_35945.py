# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with variable_scope.variable_scope(
        None, default_name="default", auxiliary_name_scope=False) as scope:
        self.assertEqual(scope.original_name_scope, "")
        self.assertEqual(
            variable_scope.get_variable("w", []).name, "default/w:0")
        self.assertEqual(constant_op.constant([], name="c").name, "c:0")
    # Recheck: new name scope is NOT created before
    with ops.name_scope("default"):
        self.assertEqual(
            constant_op.constant([], name="c").name, "default/c:0")

    with variable_scope.variable_scope("outer"):
        with variable_scope.variable_scope(
            None, default_name="default",
            auxiliary_name_scope=False) as inner:
            self.assertEqual(inner.original_name_scope, "outer/")
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/default/w:0")
            self.assertEqual(
                constant_op.constant([], name="c").name, "outer/c:0")
        # Recheck: new name scope is NOT created before
        with ops.name_scope("default"):
            self.assertEqual(
                constant_op.constant([], name="c").name, "outer/default/c:0")
