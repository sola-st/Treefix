# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
context = trace_type.InternalTracingContext()
tensor = array_ops.zeros([11, 3, 5],
                         dtype=dtypes.int32).__tf_tracing_type__(context)
spec = tensor_spec.TensorSpec(
    [11, 3, 5], dtype=dtypes.int32).__tf_tracing_type__(context)
spec_with_name = tensor_spec.TensorSpec(
    [11, 3, 5], dtype=dtypes.int32,
    name='name').__tf_tracing_type__(context)

self.assertEqual(tensor, spec)
self.assertNotEqual(tensor, spec_with_name)
