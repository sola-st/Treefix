# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/immutable_dict_test.py
d = immutable_dict.ImmutableDict({'x': 1, 'y': 2})
with self.assertRaises(TypeError):
    del d['x']  # pylint: disable=unsupported-delete-operation
with self.assertRaises(TypeError):
    del d['z']  # pylint: disable=unsupported-delete-operation
