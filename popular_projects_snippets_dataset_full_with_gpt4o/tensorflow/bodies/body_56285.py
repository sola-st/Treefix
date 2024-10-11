# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/immutable_dict_test.py
d = immutable_dict.ImmutableDict({'x': 1, 'y': 2})
s = repr(d)
self.assertTrue(s == "ImmutableDict({'x': 1, 'y': 2})" or
                s == "ImmutableDict({'y': 1, 'x': 2})")
