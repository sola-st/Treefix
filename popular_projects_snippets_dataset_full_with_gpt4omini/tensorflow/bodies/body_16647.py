# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
var = resource_variable_ops.ResourceVariable(
    initial_value=initial_value,
    shape=shape,
    dtype=dtype,
    trainable=trainable)
spec = resource_variable_ops.VariableSpec.from_value(var)
self.assertEqual(spec.shape, shape)
self.assertEqual(spec.dtype, dtype)
self.assertEqual(spec.trainable, trainable)
self.assertIsNone(spec.alias_id)
