# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity_test.py
a = object_identity._ObjectIdentityWrapper('a')
b = object_identity._ObjectIdentityWrapper('b')
c = object_identity._ObjectIdentityWrapper('c')
flat = nest.flatten([[[(a, b)]], c])
self.assertEqual(flat, [a, b, c])
