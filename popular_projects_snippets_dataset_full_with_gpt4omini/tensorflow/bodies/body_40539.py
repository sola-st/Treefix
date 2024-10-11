# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
graph = ops.Graph()
with graph.as_default(), context.graph_mode():
    array_ops.placeholder(dtypes.int32)
self.assertLen(graph.get_operations(), 1)
