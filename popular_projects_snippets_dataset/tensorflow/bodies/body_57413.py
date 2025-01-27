# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Find all children hints.

  For a given OpHint, we find all children hints inside it, we also copy all the
  nodes inside function defs (if applicable) to the original graph_def, they are
  returned in a list as well.

  Args:
    call: Parent OpHint that contains children ophints.
    graph_def: Original graph def.

  Returns:
    Ordered children hints inside the parent ophint; new graph def that contains
    nodes inside function defs (if applicable); nodes inside function defs.
  """
name_to_input_name, _, _ = _extract_graph_summary(graph_def)
input_names, output_names = call.flattened_inputs_and_outputs()

reachable_by_input = _bfs_for_reachable_nodes(input_names, name_to_input_name)
reachable_by_output = _bfs_for_reachable_nodes(output_names,
                                               name_to_input_name)
output_nodes_set = set(output_names)
children_hints = []
out = _graph_pb2.GraphDef()
out.library.CopyFrom(graph_def.library)
out.versions.CopyFrom(graph_def.versions)
function_def_nodes = set()
for node in graph_def.node:
    out.node.extend([_copy.deepcopy(node)])
    n = _tensor_name_base(node.name)
    if n in reachable_by_output:
        if n not in reachable_by_input and n not in output_nodes_set:
            # special handle for while loop function def.
            if node.op == "While" or node.op == "StatelessWhile":
                body_name = node.attr["body"].func.name
                inputs_outside_loop = node.input
                for function_def in graph_def.library.function:
                    if function_def.signature.name == body_name:
                        function_inputs = function_def.signature.input_arg
                        assert len(inputs_outside_loop) == len(function_inputs)
                        nodes_mapping = {}
                        for i, function_input in enumerate(function_inputs):
                            nodes_mapping[function_input.name] = inputs_outside_loop[i]
                        (children_hints_in_loop,
                         new_nodes) = _find_children_hints_in_while_loop(
                             function_def, nodes_mapping)
                        function_def_nodes.update([x.name for x in new_nodes])
                        children_hints.extend(children_hints_in_loop)
                        out.node.extend(new_nodes)

exit((children_hints, out, function_def_nodes))
