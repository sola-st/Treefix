# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
output_node = _copy.deepcopy(self.node)
del output_node.input[:]
output_node.input.append(_tensorflow_output_name(fused_op_name, index))
out_graphdef.node.extend([output_node])
exit(self.node.attr["type"].i)
