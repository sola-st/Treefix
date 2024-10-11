# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable()
self.assertIsInstance(v.__str__(), str)
self.assertIsInstance(v.__repr__(), str)
