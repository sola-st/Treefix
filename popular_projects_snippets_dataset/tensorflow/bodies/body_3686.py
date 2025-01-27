# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
attrs_a = default_types.Attrs.from_type_and_attributes(
    TestAttrsClass, (MockSupertypes2With3(1), MockSupertypes2With3(2),
                     MockSupertypes2With3(3)))
attrs_b = default_types.Attrs.from_type_and_attributes(
    TestAttrsClass, (MockSupertypes2With3(2), MockSupertypes2With3(2),
                     MockSupertypes2With3(2)))

self.assertEqual(attrs_a, attrs_a.most_specific_common_supertype([]))
self.assertIsNone(attrs_a.most_specific_common_supertype([attrs_b]))
self.assertEqual(
    attrs_b.most_specific_common_supertype([attrs_a]),
    default_types.Attrs.from_type_and_attributes(
        TestAttrsClass, (MockSupertypes2With3(3), MockSupertypes2With3(3),
                         MockSupertypes2With3(3))))
