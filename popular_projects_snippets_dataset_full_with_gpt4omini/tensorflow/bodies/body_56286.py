# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/immutable_dict_test.py
d = immutable_dict.ImmutableDict({'x': 1, 'y': 2})
self.assertEqual(d.get('x'), 1)
self.assertEqual(d.get('y'), 2)
self.assertIsNone(d.get('z'))
self.assertEqual(d.get('z', 'Foo'), 'Foo')
