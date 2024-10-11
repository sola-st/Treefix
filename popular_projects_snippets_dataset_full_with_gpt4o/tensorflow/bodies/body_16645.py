# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
spec = VariableSpec(shape=(None, None, None))
self.assertIsNone(spec.name)
self.assertAllEqual(spec.shape.as_list(), [None, None, None])
self.assertEqual(spec.dtype, dtypes.float32)
self.assertTrue(spec.trainable)
self.assertIs(spec.value_type, resource_variable_ops.ResourceVariable)
self.assertAllEqual(spec._component_specs,
                    [tensor_spec.TensorSpec([], dtypes.resource)])

spec2 = VariableSpec(shape=(1, 2, 3), dtype=dtypes.float64,
                     trainable=False)
self.assertEqual(spec2.shape.as_list(), [1, 2, 3])
self.assertEqual(spec2.dtype, dtypes.float64)
self.assertFalse(spec2.trainable)
self.assertIs(spec2.value_type, resource_variable_ops.ResourceVariable)
self.assertAllEqual(spec2._component_specs,
                    [tensor_spec.TensorSpec([], dtypes.resource)])
