# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
# The function module doesn't support recursive functions, so we build a
# recursive function situation by ourselves: A calls B calls A and Const.
graph = graph_pb2.GraphDef()
a = graph.library.function.add()
b = graph.library.function.add()
a.signature.name = "A"
b.signature.name = "B"
a.node_def.add().op = "B"
b.node_def.add().op = "Const"
b.node_def.add().op = "A"

# Use A in the graph
graph.node.add().op = "A"

# The stripped op list should contain just Const.
op_list = meta_graph.stripped_op_list_for_graph(graph)
self.assertEqual(["Const"], [op.name for op in op_list.op])
