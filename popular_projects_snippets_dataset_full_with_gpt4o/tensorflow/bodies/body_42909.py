# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
"""Packing orders dicts by key, including OrderedDicts."""
custom = mapping_type([("d", 0), ("b", 0), ("a", 0), ("c", 0)])
plain = {"d": 0, "b": 0, "a": 0, "c": 0}
seq = [0, 1, 2, 3]
custom_reconstruction = nest.pack_sequence_as(custom, seq)
plain_reconstruction = nest.pack_sequence_as(plain, seq)
self.assertIsInstance(custom_reconstruction, mapping_type)
self.assertIsInstance(plain_reconstruction, dict)
self.assertEqual(
    mapping_type([("d", 3), ("b", 1), ("a", 0), ("c", 2)]),
    custom_reconstruction)
self.assertEqual({"d": 3, "b": 1, "a": 0, "c": 2}, plain_reconstruction)
