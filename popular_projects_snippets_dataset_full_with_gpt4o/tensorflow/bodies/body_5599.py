# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(constraint=lambda x: x + 1.)
self.assertEqual(v.constraint(1.), 2.)
