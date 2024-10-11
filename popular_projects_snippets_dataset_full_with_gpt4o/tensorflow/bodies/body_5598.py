# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(1.)
self.assertEqual(self.evaluate(v.initial_value), 1.)
