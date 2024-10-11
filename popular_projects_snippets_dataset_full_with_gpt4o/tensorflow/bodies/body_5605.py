# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable([1.])
self.assertEqual(ops.convert_to_tensor(v), [1.])
