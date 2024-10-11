# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
init = init_ops.constant_initializer(0.3)
with variable_scope.variable_scope("tower0") as tower:
    with variable_scope.variable_scope("foo", initializer=init):
        v = variable_scope.get_variable("v", [])
        self.evaluate(variables_lib.variables_initializer([v]))
        self.assertAllClose(self.evaluate(v.value()), 0.3)
    with variable_scope.variable_scope(tower, initializer=init):
        w = variable_scope.get_variable("w", [])
        self.evaluate(variables_lib.variables_initializer([w]))
        self.assertAllClose(self.evaluate(w.value()), 0.3)
