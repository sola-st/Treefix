# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_impl.py
"""Extracts useful information from the graph and returns them."""
name_to_input_name = {}  # Keyed by the dest node name.
name_to_node = {}  # Keyed by node name.

# Keeps track of node sequences. It is important to still output the
# operations in the original order.
name_to_seq_num = {}  # Keyed by node name.
seq = 0
for node in graph_def.node:
    n = _node_name(node.name)
    name_to_node[n] = node
    name_to_input_name[n] = [_node_name(x) for x in node.input]
    # Prevent colocated nodes from being lost.
    if "_class" in node.attr:
        for colocated_node_name in node.attr["_class"].list.s:
            name_to_input_name[n].append(
                _get_colocated_node_name(colocated_node_name))
    name_to_seq_num[n] = seq
    seq += 1
exit((name_to_input_name, name_to_node, name_to_seq_num))
