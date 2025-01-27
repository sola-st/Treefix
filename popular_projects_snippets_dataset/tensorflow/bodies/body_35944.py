# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    with variable_scope.variable_scope(
        "scope", auxiliary_name_scope=False) as scope:
        self.assertEqual(scope.original_name_scope, "")
        self.assertEqual(
            variable_scope.get_variable("w", []).name, "scope/w:0")
        self.assertEqual(constant_op.constant([], name="c").name, "c:0")
    with variable_scope.variable_scope(scope, auxiliary_name_scope=False):
        self.assertEqual(scope.original_name_scope, "")
        self.assertEqual(
            variable_scope.get_variable("w1", []).name, "scope/w1:0")
        self.assertEqual(constant_op.constant([], name="c1").name, "c1:0")
    # Recheck: new name scope is NOT created before
    with ops.name_scope("scope"):
        self.assertEqual(constant_op.constant([], name="c").name, "scope/c:0")

    with variable_scope.variable_scope("outer"):
        with variable_scope.variable_scope(
            "inner", auxiliary_name_scope=False) as inner:
            self.assertEqual(inner.original_name_scope, "outer/")
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/inner/w:0")
            self.assertEqual(
                constant_op.constant([], name="c").name, "outer/c:0")
        with variable_scope.variable_scope(
            inner, auxiliary_name_scope=False) as inner1:
            self.assertEqual(inner1.original_name_scope, "outer/")
            self.assertEqual(
                variable_scope.get_variable("w1", []).name, "outer/inner/w1:0")
            self.assertEqual(
                constant_op.constant([], name="c1").name, "outer/c1:0")
        # Recheck: new name scope is NOT created before
        with ops.name_scope("inner"):
            self.assertEqual(
                constant_op.constant([], name="c").name, "outer/inner/c:0")
