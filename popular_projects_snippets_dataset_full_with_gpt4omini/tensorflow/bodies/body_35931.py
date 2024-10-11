# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
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
