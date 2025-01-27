# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Find children hints and all nodes inside the while loop.

  Args:
    function_def: Function def of the while loop.
    nodes_mapping: While loop input_arg : real node name.

  Returns:
    Ordered children hints and all re-mapped nodes inside the while loop.
  """
new_nodes = []

# Make nodes inside function def inputs point to the real nodes.
for node in function_def.node_def:
    for i, _ in enumerate(node.input):
        if node.input[i] in nodes_mapping:
            node.input[i] = nodes_mapping[node.input[i]]
    new_nodes.append(_copy.deepcopy(node))
name_to_seq_num = _extract_topology_sequence_mapping(function_def.node_def)
children_hints = _find_all_hints_in_nodes(new_nodes)
children_hints_q = []
# Ordered by the outputs.
for hint in children_hints.values():
    _, output_names = hint.flattened_inputs_and_outputs()
    seq = name_to_seq_num[output_names[0]]
    for output_name in output_names:
        seq = min(seq, name_to_seq_num[output_name])
    children_hints_q.append((seq, hint))
children_hints_q.sort(key=lambda tup: tup[0])
ordered_children_hints = [x[1] for x in children_hints_q]
exit((ordered_children_hints, new_nodes))
