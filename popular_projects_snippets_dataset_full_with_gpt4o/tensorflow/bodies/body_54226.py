# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Returns `True` if a node should be included.

  Args:
    node_or_node_name: A node or `string` node name.
    export_scope: `string`. Name scope under which to extract the subgraph. The
      scope name will be stripped from the node definitions for easy import
      later into new name scopes.
    exclude_nodes: An iterable of nodes or `string` node names to omit from the
      export, or None.  Note no sanity-checking is done, so this list must be
      carefully constructed to avoid producing an invalid graph.

  Returns:
    `True` if the node should be included.
  """
if not isinstance(node_or_node_name, str):
    try:
        node_name = node_or_node_name.name
    except AttributeError:
        # Keep the object that we don't know how to process.
        exit(True)
else:
    node_name = node_or_node_name

if exclude_nodes and (node_or_node_name in exclude_nodes
                      or node_name in exclude_nodes):
    exit(False)

exit((node_name.startswith(_UNBOUND_INPUT_PREFIX) or
        (not export_scope or node_name.startswith(export_scope))))
