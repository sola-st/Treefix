# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
placeholder_context = trace_type.InternalPlaceholderContext(
    ops.get_default_graph())
spec = tensor_spec.TensorSpec([1], np.float32)
placeholder = spec.placeholder_value(placeholder_context)
self.assertEqual(placeholder.name, "Placeholder:0")
self.assertEqual(placeholder.dtype, spec.dtype)
self.assertEqual(placeholder.shape, spec.shape)
