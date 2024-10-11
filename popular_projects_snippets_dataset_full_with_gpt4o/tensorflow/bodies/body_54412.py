# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
a = g0.create_op("A", [], [dtypes.float32])
b = g0.create_op("B", [], [dtypes.float32])
self._testGraphElements([a, b])
