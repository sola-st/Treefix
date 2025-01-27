# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
self.assertEqual(
    trace_type.from_value([
        tensor_spec.TensorSpec(shape=None),
        tensor_spec.TensorSpec(shape=None)
    ], trace_type.InternalTracingContext(is_legacy_signature=True)),
    default_types.List(
        tensor_spec.TensorSpec(shape=None),
        tensor_spec.TensorSpec(shape=None)))
