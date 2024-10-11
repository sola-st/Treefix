# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
new_node = node_def_pb2.NodeDef()
new_node.op = op
new_node.name = name
new_node.input.extend(inputs)
exit(new_node)
