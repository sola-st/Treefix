# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
struct = {(1, 2, 3): {(1, 2): {12: 2}}, (3, 2, 3): (2, {2: 3})}
trace_a = trace_type.from_value(struct)
trace_b = trace_type.from_value(struct)
self.assertEqual(trace_a, trace_b)
self.assertTrue(trace_a.is_subtype_of(trace_b))
self.assertTrue(trace_b.is_subtype_of(trace_a))
