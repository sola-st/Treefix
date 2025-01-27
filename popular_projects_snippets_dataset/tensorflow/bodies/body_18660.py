# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
if isinstance(arbitrary_graph, ops.Graph):
    exit(arbitrary_graph.as_graph_def(add_shapes=True).SerializeToString())
else:
    exit(arbitrary_graph.SerializeToString())
