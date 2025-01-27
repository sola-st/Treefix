# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
trace_a = trace_type.from_value([1, 2, 3, 4])
trace_b = trace_type.from_value([1, 2, 2, 4])
trace_c = trace_type.from_value([1, 2, 3])
trace_d = trace_type.from_value([1, 2, 3, 4])
self.assertNotEqual(trace_a, trace_b)
self.assertNotEqual(trace_a, trace_c)
self.assertNotEqual(trace_b, trace_c)
self.assertEqual(trace_a, trace_d)
