# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
var = resource_variable_ops.ResourceVariable(
    initial_value=initial_value,
    shape=shape,
    dtype=dtype,
    trainable=trainable)
if not context.executing_eagerly():
    self.evaluate(var.initializer)

spec = resource_variable_ops.VariableSpec.from_value(var)
components = spec._to_components(var)
self.assertIsInstance(components, list)
self.assertLen(components, 1)
self.assertIs(components[0], var.handle)
rebuilt_var = spec._from_components(components)
self.assertAllEqual(rebuilt_var.read_value(), var.read_value())
self.assertEqual(rebuilt_var.trainable, trainable)
