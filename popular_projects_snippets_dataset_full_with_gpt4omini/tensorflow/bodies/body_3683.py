# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
tuple_a = default_types.Tuple(
    MockSupertypes2With3(1), MockSupertypes2With3(2),
    MockSupertypes2With3(3))
tuple_b = default_types.Tuple(
    MockSupertypes2With3(2), MockSupertypes2With3(2),
    MockSupertypes2With3(2))

self.assertEqual(tuple_a, tuple_a.most_specific_common_supertype([]))
self.assertIsNone(tuple_a.most_specific_common_supertype([tuple_b]))
self.assertEqual(
    tuple_b.most_specific_common_supertype([tuple_a]),
    default_types.Tuple(
        MockSupertypes2With3(3), MockSupertypes2With3(3),
        MockSupertypes2With3(3)))
