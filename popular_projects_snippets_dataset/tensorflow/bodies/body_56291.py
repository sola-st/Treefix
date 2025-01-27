# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/immutable_dict_test.py
d = immutable_dict.ImmutableDict({'x': 1, 'y': 2})
self.assertNotEqual(d, {'x': 1})
