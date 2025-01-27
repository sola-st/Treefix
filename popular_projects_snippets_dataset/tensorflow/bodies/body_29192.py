# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest_test.py
"""Packing orders dicts by key, including OrderedDicts."""
ordered = collections.OrderedDict([("d", 0), ("b", 0), ("a", 0), ("c", 0)])
plain = {"d": 0, "b": 0, "a": 0, "c": 0}
seq = [0, 1, 2, 3]
ordered_reconstruction = nest.pack_sequence_as(ordered, seq)
plain_reconstruction = nest.pack_sequence_as(plain, seq)
self.assertEqual(
    collections.OrderedDict([("d", 3), ("b", 1), ("a", 0), ("c", 2)]),
    ordered_reconstruction)
self.assertEqual({"d": 3, "b": 1, "a": 0, "c": 2}, plain_reconstruction)
