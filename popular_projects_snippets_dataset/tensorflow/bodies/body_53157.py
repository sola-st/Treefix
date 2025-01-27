# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
graph_def1 = graph_pb2.GraphDef()
graph_def1.node.extend([
    self.create_constant_node_def(
        "C", float("nan"), dtypes.float32, inputs=["^I"]),
    self.create_node_def("Identity", "I", ["Base"]),
    self.create_node_def("BaseOp", "Base", [])
])

graph_def2 = graph_pb2.GraphDef()
graph_def2.node.extend([
    self.create_constant_node_def(
        "C", float("nan"), dtypes.float32, inputs=["^I"]),
    self.create_node_def("Identity", "I", ["Base"]),
    self.create_node_def("BaseOp", "Base", [])
])
self.assertTrue(
    graph_util.graph_defs_equal(
        graph_def1, graph_def2, treat_nan_as_equal=True))
