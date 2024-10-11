# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable([1.])
self.evaluate(v.initializer)
self.assertIsInstance(v, composite_tensor.CompositeTensor)
spec = type_spec.type_spec_from_value(v)

self.assertIsInstance(spec, resource_variable_ops.VariableSpec)
self.assertAllEqual(spec.shape.as_list(), (1,))
self.assertEqual(spec.dtype, dtypes.float32)
self.assertTrue(spec.trainable)
self.assertEqual(spec, v._type_spec)
self.assertEqual(spec, v._shape_invariant_to_type_spec((1,)))
