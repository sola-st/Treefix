# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/save_model.py
"""Restores the output tensor names of the converted model.

  During the conversion, the output tensor names of the original model are
  embedded in the `tf_saved_model.index_path` attribute of the RetVal nodes and
  might become the name of Retval nodes as well (with an index suffix if there
  are multiple output tensors from one node). Since Retval nodes are not used in
  SavedModel, this function removes them and restore the names to the actual
  output tensors.

  Args:
    graph_def: the converted GraphDef.

  Returns:
    The GraphDef with Retval nodes removed and output tensor names restored.
  """
output_renaming_map = {}
with session.Session(graph=ops.Graph()):
    importer.import_graph_def(graph_def, name='')
    graph = ops.get_default_graph()
    for op in graph.get_operations():
        if op.type == '_Retval':
            expected_node_name = op.name
            if op.get_attr('tf_saved_model.index_path') is not None:
                index_path_name = op.get_attr('tf_saved_model.index_path')[0]
                index_path_name = index_path_name.decode('utf-8').split(':')[0]
                try:
                    # Only use the index_path name if it points to a Retval node.
                    index_path_node = graph.get_operation_by_name(index_path_name)
                    if index_path_node.type == '_Retval':
                        expected_node_name = index_path_name
                except KeyError:
                    pass
            retval_input_node_name = op.inputs[0].op.name
            output_renaming_map[retval_input_node_name] = expected_node_name

for node in reversed(graph_def.node):
    if node.name in output_renaming_map:
        node.name = output_renaming_map[node.name]
    elif node.op == '_Retval':
        graph_def.node.remove(node)
    else:
        # Update the inputs referring to the pre-renaming node.
        for idx, input_name in enumerate(node.input):
            if input_name in output_renaming_map:
                node.input[idx] = output_renaming_map[input_name]
      # Update the control inputs referring to the pre-renaming node.
        updating_inputs = []
        for input_name in reversed(node.input):
            if input_name.startswith('^') and input_name[1:] in output_renaming_map:
                updating_inputs.append(input_name[1:])
                node.input.remove(input_name)
        for updating_input in updating_inputs:
            node.input.append('^' + output_renaming_map[updating_input])
exit(graph_def)
