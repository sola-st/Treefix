# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
dict_type = default_types.Dict
dict_a = dict_type({
    'a': MockSupertypes2With3(1),
    'b': MockSupertypes2With3(2),
    'c': MockSupertypes2With3(3)
})
dict_b = dict_type({
    'a': MockSupertypes2With3(2),
    'b': MockSupertypes2With3(2),
    'c': MockSupertypes2With3(2)
})

self.assertEqual(dict_a, dict_a.most_specific_common_supertype([]))
self.assertIsNone(dict_a.most_specific_common_supertype([dict_b]))
self.assertEqual(
    dict_b.most_specific_common_supertype([dict_a]),
    dict_type({
        'a': MockSupertypes2With3(3),
        'b': MockSupertypes2With3(3),
        'c': MockSupertypes2With3(3)
    }))
