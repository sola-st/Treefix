# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable(synchronization=synchronization)
self.assertEqual(v.synchronization, synchronization)
