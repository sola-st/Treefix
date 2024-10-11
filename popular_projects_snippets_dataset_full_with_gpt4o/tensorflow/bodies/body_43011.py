# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity_test.py
a = object()
b = object()
set1 = object_identity.ObjectIdentitySet([a, b])
set1.clear()
self.assertLen(set1, 0)
