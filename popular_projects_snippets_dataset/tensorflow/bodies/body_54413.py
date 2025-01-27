# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
a = g0.create_op("A", [], [dtypes.float32])
b = g0.create_op("B", [], [dtypes.float32])
sparse = sparse_tensor.SparseTensor(
    _apply_op(g0, "Int64Output", [], [dtypes.int64]),
    _apply_op(g0, "FloatOutput", [], [dtypes.float32]),
    _apply_op(g0, "Int64Output", [], [dtypes.int64]))
self._testGraphElements([a, sparse, b])
