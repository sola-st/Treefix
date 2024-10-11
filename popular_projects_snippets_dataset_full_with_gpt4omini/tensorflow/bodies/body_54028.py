# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
graph_def = graph_pb2.GraphDef()
node_foo = graph_def.node.add()
node_foo.name = "foo"
self.assertIs(test_util.get_node_def_from_graph("foo", graph_def), node_foo)
self.assertIsNone(test_util.get_node_def_from_graph("bar", graph_def))
