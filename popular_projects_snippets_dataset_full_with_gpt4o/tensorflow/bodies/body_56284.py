# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/immutable_dict_test.py
d1 = immutable_dict.ImmutableDict({})
self.assertLen(d1, 0)  # pylint: disable=g-generic-assert
d2 = immutable_dict.ImmutableDict({'x': 1, 'y': 2})
self.assertLen(d2, 2)
