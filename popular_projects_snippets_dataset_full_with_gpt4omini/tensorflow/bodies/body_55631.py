# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
# Function A calls B via StatefulPartitionedCall.
graph = graph_pb2.GraphDef()
a = graph.library.function.add()
b = graph.library.function.add()
a.signature.name = "A"
b.signature.name = "B"
node_in_a = a.node_def.add()
node_in_a.op = "StatefulPartitionedCall"
node_in_a.attr["f"].func.name = "B"
b.node_def.add().op = "Const"
b.node_def.add().op = "A"

# Use A in the graph via PartitionedCall.
node = graph.node.add()
node.op = "PartitionedCall"
node.attr["f"].func.name = "A"

op_list = meta_graph.stripped_op_list_for_graph(graph)
self.assertSameElements(
    ["Const", "PartitionedCall", "StatefulPartitionedCall"],
    [op.name for op in op_list.op])
