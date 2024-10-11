# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
"""`flatten` orders dicts by key, including OrderedDicts."""
ordered = mapping_type([("d", 3), ("b", 1), ("a", 0), ("c", 2)])
plain = {"d": 3, "b": 1, "a": 0, "c": 2}
ordered_flat = nest.flatten(ordered)
plain_flat = nest.flatten(plain)
self.assertEqual([0, 1, 2, 3], ordered_flat)
self.assertEqual([0, 1, 2, 3], plain_flat)
