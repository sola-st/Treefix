# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
self.assertIsInstance(v.assign(1., read_value=False), ops.Operation)
self.assertIsInstance(v.assign_add(1., read_value=False), ops.Operation)
self.assertIsInstance(v.assign_sub(1., read_value=False), ops.Operation)
