# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
with g0.as_default():
    variable = variables.Variable([1.0])
a = g0.create_op("A", [], [dtypes.float32])
b = g0.create_op("B", [], [dtypes.float32])
self._testGraphElements([a, variable, b])
