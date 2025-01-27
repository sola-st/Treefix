# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
graph_def = graph_pb2.GraphDef()
n1 = graph_def.node.add()
n1.name = "n1"
with self.assertRaisesRegex(TypeError, "must be an iterable"):
    graph_util.extract_sub_graph(graph_def, "n1")
