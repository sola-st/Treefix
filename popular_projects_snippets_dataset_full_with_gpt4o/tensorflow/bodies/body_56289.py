# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/immutable_dict_test.py
d = immutable_dict.ImmutableDict({'x': 1, 'y': 2})
self.assertEqual(set(d.items()), set([('x', 1), ('y', 2)]))
