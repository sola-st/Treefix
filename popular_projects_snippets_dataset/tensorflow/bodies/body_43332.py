# Extracted from ./data/repos/tensorflow/tensorflow/python/util/type_annotations_test.py
self.assertEqual(
    type_annotations.is_generic_union(tp), expected == 'Union')
self.assertEqual(
    type_annotations.is_generic_tuple(tp), expected == 'Tuple')
self.assertEqual(
    type_annotations.is_generic_mapping(tp), expected == 'Mapping')
