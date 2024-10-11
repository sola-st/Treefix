# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

graph_str = "node { name: 'w1' op: 'params' }"
graph_def = graph_pb2.GraphDef()
text_format.Merge(graph_str, graph_def)

# test string based comparison
self.assertProtoEquals(graph_str, graph_def)

# test original comparison
self.assertProtoEquals(graph_def, graph_def)
