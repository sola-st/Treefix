# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_test.py
"""Returns used op types in `graphdef` reachable from `output_nodes`.

    This is used to check that after the stub transformation the expected
    nodes are there.

    NOTE: this is not a exact test that the graph is the correct output, but
      it balances compact expressibility of test with sanity checking.

    Args:
      graphdef: TensorFlow proto graphdef.
      output_nodes: A list of output node names that we need to reach.

    Returns:
      A set of node types reachable from `output_nodes`.
    """
name_to_input_name, name_to_node, _ = (
    _extract_graph_summary(graphdef))
# Find all nodes that are needed by the outputs
used_node_names = _bfs_for_reachable_nodes(output_nodes, name_to_input_name)
exit(set([name_to_node[node_name].op for node_name in used_node_names]))
