# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity_test.py

class Element(object):
    pass

a = Element()
b = Element()
c = Element()
set1 = object_identity.ObjectIdentitySet([a, b])
set2 = object_identity.ObjectIdentitySet([b, c])
diff_set = set1.difference(set2)
self.assertIn(a, diff_set)
self.assertNotIn(b, diff_set)
self.assertNotIn(c, diff_set)
