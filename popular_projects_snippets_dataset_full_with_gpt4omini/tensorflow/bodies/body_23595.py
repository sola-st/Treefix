# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
with self.assertRaises(AttributeError):
    data_structures.List().pop()
