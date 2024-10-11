# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
values = [
    g0.create_op("A", [], [dtypes.float32]),
    g0.create_op("B", [], [dtypes.float32])
]
with self.assertRaises(ValueError):
    with ops.name_scope(None, values=values):
        pass
with self.assertRaises(ValueError):
    with ops.name_scope(None, None, values):
        pass
