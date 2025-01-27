# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
literal = default_types.Literal

list_a = default_types.List(literal(1), literal(2), literal(3))
list_b = default_types.List(literal(1), literal(2), literal(3))

tuple_a = default_types.Tuple(literal(1), literal(2), literal(3))
tuple_b = default_types.Tuple(literal(1), literal(2), literal(3))

self.assertEqual(list_a, list_b)
self.assertEqual(tuple_a, tuple_b)
self.assertNotEqual(list_a, tuple_a)
self.assertNotEqual(tuple_a, list_a)
