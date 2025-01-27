# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
placeholder_context = trace_type.InternalPlaceholderContext()
composite_value = [1, 2, (3, [4, 5]), {6: [7]}, TestAttrsClass(8, (10, 11))]
composite_type = trace_type.from_value(composite_value)
placeholder_value = composite_type.placeholder_value(placeholder_context)
self.assertEqual(composite_value, placeholder_value)
