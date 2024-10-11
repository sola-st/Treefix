# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(1.)
w = self.create_variable(2.)
x = self.create_variable(1.)
self.assertEqual(v, x)
self.assertNotEqual(v, w)
