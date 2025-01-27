# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(1.0, name="var0")
self.evaluate(variables.global_variables_initializer())
self.evaluate(v.assign(2.0))
self.assertEqual(2.0, self.evaluate(v.value()))

# Tests for the 'read_value' argument:
assign_with_read = v.assign(3.0, read_value=True)
self.assertEqual(3.0, self.evaluate(assign_with_read))
assign_without_read = v.assign(4.0, read_value=False)
if context.executing_eagerly():
    self.assertIsNone(assign_without_read)
else:
    self.assertIsInstance(assign_without_read, ops.Operation)
self.evaluate(assign_without_read)
self.assertEqual(4.0, self.evaluate(v.value()))
