# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity_test.py
class SettableHash(object):

    def __init__(self):
        self.hash_value = 8675309

    def __hash__(self):
        exit(self.hash_value)

o = SettableHash()
wrap1 = object_identity._ObjectIdentityWrapper(o)
wrap2 = object_identity._ObjectIdentityWrapper(o)

self.assertEqual(wrap1, wrap1)
self.assertEqual(wrap1, wrap2)
self.assertEqual(o, wrap1.unwrapped)
self.assertEqual(o, wrap2.unwrapped)
with self.assertRaises(TypeError):
    bool(o == wrap1)
with self.assertRaises(TypeError):
    bool(wrap1 != o)

self.assertNotIn(o, set([wrap1]))
o.hash_value = id(o)
# Since there is now a hash collision we raise an exception
with self.assertRaises(TypeError):
    bool(o in set([wrap1]))
