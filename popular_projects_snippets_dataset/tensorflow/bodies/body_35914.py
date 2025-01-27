# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
v = variable_scope.get_variable("v4", initializer=4, dtype=dtypes.int32)
self.evaluate(variables_lib.variables_initializer([v]))
self.assertAllClose(self.evaluate(v.value()), 4)

w = variable_scope.get_variable(
    "w4", initializer=numpy.array([1, 2, 3]), dtype=dtypes.int64)
self.evaluate(variables_lib.variables_initializer([w]))
self.assertAllClose(self.evaluate(w.value()), [1, 2, 3])

# A quirk to be revisited?
error = ValueError if context.executing_eagerly() else TypeError
with self.assertRaises(error):
    variable_scope.get_variable("x4", initializer={})
