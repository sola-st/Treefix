# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
context = trace_type.InternalTracingContext()
spec_1 = tensor_spec.TensorSpec(
    None, dtype=dtypes.int32).__tf_tracing_type__(context)
spec_2 = tensor_spec.TensorSpec(
    None, dtype=dtypes.int32).__tf_tracing_type__(context)
self.assertEqual(spec_1, spec_2)
