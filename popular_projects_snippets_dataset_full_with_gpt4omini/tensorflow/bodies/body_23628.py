# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
mapping = data_structures.Mapping()
with self.assertRaises(TypeError):
    mapping[1] = data_structures.List()
