# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
# In legacy graph mode, tensor equality is object equality
v = self.create_variable(1.)
w = self.create_variable(1.)
self.assertNotEqual(v, w)
self.assertEqual(v, v)
