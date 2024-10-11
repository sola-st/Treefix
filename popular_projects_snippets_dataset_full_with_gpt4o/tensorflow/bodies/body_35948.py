# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
# Github issue: #13429
with self.cached_session():
    with variable_scope.variable_scope("outer"):
        with variable_scope.variable_scope("inner") as inner:
            pass

    with variable_scope.variable_scope(
        inner, auxiliary_name_scope=False) as scope:
        with ops.name_scope(scope.original_name_scope):
            self.assertEqual(
                variable_scope.get_variable("w", []).name, "outer/inner/w:0")
            self.assertEqual(
                constant_op.constant([], name="c").name, "outer/inner/c:0")
        with ops.name_scope("inner"):
            self.assertEqual(
                constant_op.constant([], name="c").name, "inner/c:0")

    with variable_scope.variable_scope("another"):
        with variable_scope.variable_scope(
            inner, auxiliary_name_scope=False) as scope1:
            with ops.name_scope(scope1.original_name_scope):
                self.assertEqual(
                    variable_scope.get_variable("w1", []).name,
                    "outer/inner/w1:0")
                self.assertEqual(
                    constant_op.constant([], name="c1").name, "outer/inner/c1:0")
            with ops.name_scope("inner"):
                self.assertEqual(
                    constant_op.constant([], name="c").name, "another/inner/c:0")
