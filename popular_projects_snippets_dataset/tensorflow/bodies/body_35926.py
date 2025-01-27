# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
# Test the get_variable_scope() function and setting properties of result.
init = init_ops.constant_initializer(0.3)
with variable_scope.variable_scope("bar"):
    new_init1 = variable_scope.get_variable_scope().initializer
    self.assertEqual(new_init1, None)
    # Check that we can set initializer like this.
    variable_scope.get_variable_scope().set_initializer(init)
    v = variable_scope.get_variable("v", [])
    self.evaluate(variables_lib.variables_initializer([v]))
    self.assertAllClose(self.evaluate(v.value()), 0.3)
    if not context.executing_eagerly():
        # Check that we can set reuse.
        variable_scope.get_variable_scope().reuse_variables()
        with self.assertRaises(ValueError):  # Fail, w does not exist yet.
            variable_scope.get_variable("w", [1])
    # Check that the set initializer goes away.
new_init = variable_scope.get_variable_scope().initializer
self.assertEqual(new_init, None)
