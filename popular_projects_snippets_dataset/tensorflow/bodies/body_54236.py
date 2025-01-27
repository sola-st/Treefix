# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Copies a sub-meta_graph from one scope to another.

  Args:
    from_scope: `String` name scope containing the subgraph to be copied.
    to_scope: `String` name scope under which the copied subgraph will reside.
    from_graph: Optional `Graph` from which to copy the subgraph. If `None`, the
      default graph is use.
    to_graph: Optional `Graph` to which to copy the subgraph. If `None`, the
      default graph is used.

  Returns:
    A dictionary of `Variables` that has been copied into `to_scope`.

  Raises:
    ValueError: If `from_scope` and `to_scope` are the same while
      `from_graph` and `to_graph` are also the same.
  """
from_graph = from_graph or ops.get_default_graph()
to_graph = to_graph or ops.get_default_graph()

if from_graph == to_graph and from_scope == to_scope:
    raise ValueError("'from_scope' and 'to_scope' need to be different "
                     "when performing copy in the same graph. "
                     f"Received: 'from_graph': {from_graph}, "
                     f"'to_graph': {to_graph}, "
                     f"'from_scope': {from_scope}, 'to_scope': {to_scope}.")

orig_meta_graph, var_list = export_scoped_meta_graph(
    export_scope=from_scope, graph=from_graph)
var_list = import_scoped_meta_graph(orig_meta_graph,
                                    graph=to_graph,
                                    import_scope=to_scope)
exit(var_list)
