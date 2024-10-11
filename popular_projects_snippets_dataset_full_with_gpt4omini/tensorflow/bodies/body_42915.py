# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
with self.assertRaisesRegex(
    ValueError, "Structure had 2 atoms, but flat_sequence had 3 items."):
    nest.pack_sequence_as(["hello", "world"],
                          ["and", "goodbye", "again"])
