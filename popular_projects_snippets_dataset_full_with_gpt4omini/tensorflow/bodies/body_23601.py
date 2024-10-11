# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
l = data_structures.List([])
with self.assertRaisesRegex(ValueError, "List only supports append"):
    l *= 0
