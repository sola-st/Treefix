# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
graph_def = graph_pb2.GraphDef()
n1 = graph_def.node.add()
n1.name = "n1"
n1.input.extend(["n5"])
n2 = graph_def.node.add()
n2.name = "n2"
# Take the first output of the n1 node as the input.
n2.input.extend(["n1:0"])
n3 = graph_def.node.add()
n3.name = "n3"
# Add a control input (which isn't really needed by the kernel, but
# rather to enforce execution order between nodes).
n3.input.extend(["^n2"])
n4 = graph_def.node.add()
n4.name = "n4"

# It is fine to have a loops in the graph as well.
n5 = graph_def.node.add()
n5.name = "n5"
n5.input.extend(["n1"])

sub_graph = graph_util.extract_sub_graph(graph_def, ["n3"])
self.assertEqual("n1", sub_graph.node[0].name)
self.assertEqual("n2", sub_graph.node[1].name)
self.assertEqual("n3", sub_graph.node[2].name)
self.assertEqual("n5", sub_graph.node[3].name)
