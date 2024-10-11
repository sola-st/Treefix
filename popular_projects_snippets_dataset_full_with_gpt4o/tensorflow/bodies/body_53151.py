# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
"""Check that chains of Identity nodes are correctly pruned.

    Create a chain of four nodes, A, B, C, and D where A inputs B, B inputs C,
    and C inputs D. Nodes B and C are "Identity" and should be pruned, resulting
    in the nodes A and D, where A inputs D.
    """
graph_def = graph_pb2.GraphDef()
graph_def.node.extend([
    self.create_node_def("Aop", "A", ["B"]),
    self.create_node_def("Identity", "B", ["C"]),
    self.create_node_def("Identity", "C", ["D"]),
    self.create_node_def("Dop", "D", [])
])

expected_graph_def = graph_pb2.GraphDef()
expected_graph_def.node.extend([
    self.create_node_def("Aop", "A", ["D"]),
    self.create_node_def("Dop", "D", [])
])

self.assertProtoEquals(expected_graph_def,
                       graph_util.remove_training_nodes(graph_def))
