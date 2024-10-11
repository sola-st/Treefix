# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
self.assertEqual(
    trace_type.from_value(
        {
            'a': tensor_spec.TensorSpec(shape=None),
            'b': tensor_spec.TensorSpec(shape=None)
        }, trace_type.InternalTracingContext(is_legacy_signature=True)),
    default_types.Dict({
        'a': tensor_spec.TensorSpec(shape=None),
        'b': tensor_spec.TensorSpec(shape=None)
    }))
