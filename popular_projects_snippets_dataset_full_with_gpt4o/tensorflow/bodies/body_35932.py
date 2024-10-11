# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():

    def test_value(value):
        x = constant_op.constant(value)
        with variable_scope.variable_scope(
            "testVarScopeGetOrCreateReuse_bar",
            reuse=variable_scope.AUTO_REUSE):
            _ = state_ops.assign(variable_scope.get_variable("var", []), x)
        with variable_scope.variable_scope(
            "testVarScopeGetOrCreateReuse_bar",
            reuse=variable_scope.AUTO_REUSE):
            _ = variable_scope.get_variable("var", [])
        self.assertEqual(value, self.evaluate(x))

    test_value(42.)  # Variable is created.
    test_value(13.)  # Variable is reused hereafter.
    test_value(17.)
