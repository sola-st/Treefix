# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable()
w = self.create_variable()
d = {}
with self.assertRaises(TypeError):
    d[v] = 1
d[v.ref()] = 1
self.assertEqual(d[v.ref()], 1)
self.assertNotIn(w.ref(), d)
