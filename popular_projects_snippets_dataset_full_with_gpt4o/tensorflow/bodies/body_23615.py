# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
with self.assertRaises(TypeError):
    hash(data_structures.ListWrapper())  # pylint: disable=no-value-for-parameter
