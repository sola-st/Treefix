# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
trace_a = trace_type.from_value(TestAttrsClass(1, 2))
expected = default_types.Attrs.from_type_and_attributes(
    TestAttrsClass, (default_types.Literal(1), default_types.Literal(2)))
self.assertEqual(trace_a, expected)
self.assertTrue(trace_a.is_subtype_of(trace_a))
