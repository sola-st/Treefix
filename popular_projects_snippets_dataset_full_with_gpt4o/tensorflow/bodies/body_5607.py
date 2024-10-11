# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable()
w = self.create_variable()
d = {v: 1}
self.assertEqual(d[v], 1)
self.assertNotIn(w, d)
