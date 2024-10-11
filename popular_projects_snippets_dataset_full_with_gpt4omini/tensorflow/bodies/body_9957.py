# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_test.py
new_node = node_def_pb2.NodeDef()
new_node.op = op
new_node.name = name
for input_name in inputs:
    new_node.input.extend([input_name])
exit(new_node)
