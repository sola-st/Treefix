# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
"""`flatten` orders dicts by key, including OrderedDicts."""
ordered = collections.OrderedDict([("d", 3), ("b", 1), ("a", 0), ("c", 2)])

# test flattening
ordered_keys_flat = nest.flatten(ordered.keys())
ordered_values_flat = nest.flatten(ordered.values())
ordered_items_flat = nest.flatten(ordered.items())
self.assertEqual([3, 1, 0, 2], ordered_values_flat)
self.assertEqual(["d", "b", "a", "c"], ordered_keys_flat)
self.assertEqual(["d", 3, "b", 1, "a", 0, "c", 2], ordered_items_flat)

# test packing
self.assertEqual([("d", 3), ("b", 1), ("a", 0), ("c", 2)],
                 nest.pack_sequence_as(ordered.items(), ordered_items_flat))
