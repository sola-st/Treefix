# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Removes a stack->unstack pattern from in_graph_def in a returned graph.

  Args:
    in_graph_def: Graph def to use as input.

  Returns:
    Simplified tuple (graph_def, changed_something) where changed_something
    is true if anything was done.
  """
name_to_input_name, name_to_node, name_to_seq_num = _extract_graph_summary(
    in_graph_def)
del name_to_seq_num

do_generic_pack_unpack = True

out = _graph_pb2.GraphDef()
out.library.CopyFrom(in_graph_def.library)
out.versions.CopyFrom(in_graph_def.versions)
for n in in_graph_def.node:
    node_name = _tensor_name_base(n.name)
    if not node_name.startswith("OpHintStack") and not n.op.startswith("Pack"):
        continue
    next_to_visit = [node_name]
    visited = set()

    unpack_nodes = set()
    pack_node = node_name

    # Find a pattern of unstack connected to a stack (with identities
    # in between.
    matches_pattern = True
    is_hint_created_stack = False
    while next_to_visit:
        current_node_name = next_to_visit[0]
        visited.add(current_node_name)
        del next_to_visit[0]
        node = name_to_node[current_node_name]
        is_op_hint_stack = node.name.startswith("OpHintStack")
        is_op_hint_unstack = node.name.startswith("OpHintUnstack")
        if (node.op == "Identity" or is_op_hint_stack or
            (do_generic_pack_unpack and node.op == "Pack")):
            is_hint_created_stack |= is_op_hint_stack
            next_to_visit += [
                input_node for input_node in name_to_input_name[current_node_name]
                if input_node not in visited
            ]
        elif (is_op_hint_unstack or
              (do_generic_pack_unpack and node.op == "Unpack")):
            unpack_nodes.add(node.name)
            is_hint_created_stack &= is_op_hint_unstack
        else:
            matches_pattern = False
            break
        visited.add(node.name)

    if matches_pattern and len(unpack_nodes) == 1:
        pack_node = node_name

        # Check to see if anyone depends on the intermediate identity or the
        # Unstacked form
        no_external_dependency = True
        for other_n in in_graph_def.node:
            if other_n.name in visited:
                continue
            for input_tensor in name_to_input_name[other_n.name]:
                input_op = _tensor_name_base(input_tensor)
                if input_op in visited and input_op != pack_node:
                    no_external_dependency = False
      # Proceed with the substitution if the stack/unstack pair was created
      # through hints, or that it was not, but nobody is consuming things
      # between the stack and unstack.
        if is_hint_created_stack or no_external_dependency:
            end = unpack_nodes.pop()
            end_input = name_to_node[end].input[0]
            # All nodes that depend on the final stack need to be redone to use
            for other_n in in_graph_def.node:
                node_name = _tensor_name_base(other_n.name)
                if node_name not in visited:
                    new_node = _copy.deepcopy(other_n)
                    new_node.input[:] = [
                        (end_input if stripped == pack_node else non_stripped)
                        for stripped, non_stripped in zip(name_to_input_name[node_name],
                                                          new_node.input[:])
                    ]
                    out.node.extend([new_node])
            exit((out, True))
exit((in_graph_def, False))
