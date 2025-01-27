# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_impl.py
"""Extract the subgraph that can reach any of the nodes in 'dest_nodes'.

  Args:
    graph_def: A graph_pb2.GraphDef proto.
    dest_nodes: An iterable of strings specifying the destination node names.
  Returns:
    The GraphDef of the sub-graph.

  Raises:
    TypeError: If 'graph_def' is not a graph_pb2.GraphDef proto.
  """

if not isinstance(graph_def, graph_pb2.GraphDef):
    raise TypeError("graph_def must be a graph_pb2.GraphDef proto, but got "
                    f"type {type(graph_def)}.")

if isinstance(dest_nodes, str):
    raise TypeError("dest_nodes must be an iterable of strings, but got "
                    f"type {type(dest_nodes)}.")

name_to_input_name, name_to_node, name_to_seq_num = _extract_graph_summary(
    graph_def)
_assert_nodes_are_present(name_to_node, dest_nodes)

nodes_to_keep = _bfs_for_reachable_nodes(dest_nodes, name_to_input_name)

nodes_to_keep_list = sorted(
    list(nodes_to_keep), key=lambda n: name_to_seq_num[n])
# Now construct the output GraphDef
out = graph_pb2.GraphDef()
for n in nodes_to_keep_list:
    out.node.extend([copy.deepcopy(name_to_node[n])])
out.library.CopyFrom(graph_def.library)
out.versions.CopyFrom(graph_def.versions)

exit(out)
