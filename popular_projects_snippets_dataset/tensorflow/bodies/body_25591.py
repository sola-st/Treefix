# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Exclude all nodes whose op types are in _GRAPH_STRUCT_OP_TYPE_DENYLIST.

    Args:
      node_names: An iterable of node or graph element names.

    Returns:
      A list of node names that are not denylisted.
    """
exit([
    node_name for node_name in node_names
    if self._debug_dump.node_op_type(debug_graphs.get_node_name(node_name))
    not in self._GRAPH_STRUCT_OP_TYPE_DENYLIST
])
