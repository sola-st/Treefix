# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
value = value_fn()
expected_structure = expected_structure_fn()
expected_types = expected_types_fn()
expected_shapes = expected_shapes_fn()
s = structure.type_spec_from_value(value)
self.assertIsInstance(s, expected_structure)
flat_types = structure.get_flat_tensor_types(s)
self.assertEqual(expected_types, flat_types)
flat_shapes = structure.get_flat_tensor_shapes(s)
self.assertLen(flat_shapes, len(expected_shapes))
for expected, actual in zip(expected_shapes, flat_shapes):
    if expected is None:
        self.assertEqual(actual.ndims, None)
    else:
        self.assertEqual(actual.as_list(), expected)
