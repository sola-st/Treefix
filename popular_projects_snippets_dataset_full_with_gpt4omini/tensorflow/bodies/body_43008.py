# Extracted from ./data/repos/tensorflow/tensorflow/python/util/object_identity_test.py
k = object_identity._ObjectIdentityWrapper('k')
v1 = object_identity._ObjectIdentityWrapper('v1')
v2 = object_identity._ObjectIdentityWrapper('v2')
struct = nest.map_structure(lambda a, b: (a, b), {k: v1}, {k: v2})
self.assertEqual(struct, {k: (v1, v2)})
