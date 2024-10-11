# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
graph_def = graph_util.extract_sub_graph(graph_def, output_node_names)
super(_SessionConverterData, self).__init__(
    graph_def,
    variable_names_allowlist=variable_names_allowlist,
    variable_names_denylist=variable_names_denylist)

nodes_to_convert = []
tensor_names_to_convert = []
for node in self.graph_def.node:
    if node.op in ["Variable", "VariableV2", "VarHandleOp"]:
        tensor_name = node.name
        if not self._should_convert(tensor_name):
            continue
        if node.op == "VarHandleOp":
            tensor_name = tensor_name + "/Read/ReadVariableOp"
        nodes_to_convert.append(node)
        tensor_names_to_convert.append(tensor_name + ":0")

if tensor_names_to_convert:
    converted_tensors = session.run(tensor_names_to_convert)
    for node, tensor_value in zip(nodes_to_convert, converted_tensors):
        self._tensor_data[node.name] = _TensorData(
            numpy=tensor_value, dtype=node.attr["dtype"].type, index=None)
