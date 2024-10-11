# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/immutable_dict_test.py
d = immutable_dict.ImmutableDict({'x': 1, 'y': 2})
self.assertEqual(d['x'], 1)
self.assertEqual(d['y'], 2)
with self.assertRaises(KeyError):
    d['z']  # pylint: disable=pointless-statement
