# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
literal_a = default_types.Literal(1)
literal_b = default_types.Literal(2)
literal_c = default_types.Literal(1)

self.assertEqual(literal_a, literal_a.most_specific_common_supertype([]))
self.assertEqual(literal_a,
                 literal_a.most_specific_common_supertype([literal_a]))
self.assertEqual(literal_a,
                 literal_a.most_specific_common_supertype([literal_c]))
self.assertIsNone(literal_a.most_specific_common_supertype([literal_b]))
