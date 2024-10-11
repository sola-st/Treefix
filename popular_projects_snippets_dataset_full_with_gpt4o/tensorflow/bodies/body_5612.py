# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
v = self.create_variable()
self.assertIsInstance(v.initializer, ops.Operation)
self.assertIsInstance(v.op, ops.Operation)
self.assertIsInstance(v.graph, ops.Graph)
