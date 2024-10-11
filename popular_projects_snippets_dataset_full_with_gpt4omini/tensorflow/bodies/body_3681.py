# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
list_a = default_types.List(
    MockSupertypes2With3(1), MockSupertypes2With3(2),
    MockSupertypes2With3(3))
list_b = default_types.List(
    MockSupertypes2With3(2), MockSupertypes2With3(2),
    MockSupertypes2With3(2))

self.assertEqual(list_a, list_a.most_specific_common_supertype([]))
self.assertIsNone(list_a.most_specific_common_supertype([list_b]))
self.assertEqual(
    list_b.most_specific_common_supertype([list_a]),
    default_types.List(
        MockSupertypes2With3(3), MockSupertypes2With3(3),
        MockSupertypes2With3(3)))
