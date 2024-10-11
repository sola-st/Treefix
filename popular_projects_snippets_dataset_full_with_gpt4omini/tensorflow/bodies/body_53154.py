# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
graph_def1 = graph_pb2.GraphDef()
graph_def1.node.extend([
    self.create_node_def("Identity", "I", ["Base"]),
    self.create_node_def("BaseOp", "Base", []),
    self.create_constant_node_def("C", 1, dtypes.float32, inputs=["^I"]),
])

graph_def2 = graph_pb2.GraphDef()
graph_def2.node.extend([
    self.create_constant_node_def("C", 1, dtypes.float32, inputs=["^I"]),
    self.create_node_def("Identity", "I", ["Base"]),
    self.create_node_def("BaseOp", "Base", [])
])

self.assertTrue(graph_util.graph_defs_equal(graph_def1, graph_def2))
