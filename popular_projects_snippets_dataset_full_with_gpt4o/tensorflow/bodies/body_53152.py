# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
"""Check that Identity nodes used as control inputs are not removed."""
graph_def = graph_pb2.GraphDef()
graph_def.node.extend([
    self.create_constant_node_def("C", 1, dtypes.float32, inputs=["^I"]),
    self.create_node_def("Identity", "I", ["Base"]),
    self.create_node_def("BaseOp", "Base", [])
])

self.assertProtoEquals(graph_def,
                       graph_util.remove_training_nodes(graph_def))
