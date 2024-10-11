# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
init = constant_op.constant(0.1)
w = variable_scope.get_variable("v", initializer=init)
self.evaluate(variables_lib.variables_initializer([w]))
self.assertAllClose(self.evaluate(w.value()), 0.1)

with self.assertRaisesRegex(ValueError, "shape"):
    # We disallow explicit shape specification when initializer is constant.
    variable_scope.get_variable("u", [1], initializer=init)

with variable_scope.variable_scope("foo", initializer=init):
    # Constant initializer can be passed through scopes if needed.
    v = variable_scope.get_variable("v")
    self.evaluate(variables_lib.variables_initializer([v]))
    self.assertAllClose(self.evaluate(v.value()), 0.1)

# Check that non-float32 initializer creates a non-float32 variable.
init = constant_op.constant(1, dtype=dtypes.int32)
t = variable_scope.get_variable("t", initializer=init)
self.assertEqual(t.dtype.base_dtype, dtypes.int32)

# Raise error if `initializer` dtype and `dtype` are not identical.
with self.assertRaisesRegex(ValueError, "don't match"):
    variable_scope.get_variable("s", initializer=init, dtype=dtypes.float64)
