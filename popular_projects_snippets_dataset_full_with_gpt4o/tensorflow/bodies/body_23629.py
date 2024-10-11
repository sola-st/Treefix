# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
has_mappings = set([data_structures.Mapping(),
                    data_structures.Mapping()])
self.assertEqual(2, len(has_mappings))
self.assertNotIn(data_structures.Mapping(), has_mappings)
# In contrast to Mapping, dict wrappers are not hashable
a = autotrackable.AutoTrackable()
a.d = {}
self.assertEqual({}, a.d)
self.assertFalse({} != a.d)  # pylint: disable=g-explicit-bool-comparison
self.assertNotEqual({1: 2}, a.d)
with self.assertRaisesRegex(TypeError, "unhashable"):
    set([a.d])
