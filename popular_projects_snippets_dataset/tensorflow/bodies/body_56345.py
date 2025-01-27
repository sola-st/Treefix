# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
signature_context = trace_type.InternalTracingContext()
type_1 = tensor_spec.TensorSpec(
    tensor_shape.TensorShape([1, 2, 3]), dtypes.float32,
    None).__tf_tracing_type__(signature_context)
type_2 = tensor_spec.TensorSpec(
    tensor_shape.TensorShape([1, 2, 3]), dtypes.float32,
    None).__tf_tracing_type__(signature_context)
self.assertEqual(type_1, type_1)
self.assertEqual(type_1, type_2)
self.assertTrue(type_1.is_subtype_of(type_1))
self.assertTrue(type_2.is_subtype_of(type_1))
self.assertTrue(type_1.is_subtype_of(type_2))
