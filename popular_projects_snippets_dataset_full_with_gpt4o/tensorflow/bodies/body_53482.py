# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Looks up the node's statistics function in the registry and calls it.

  This function takes a Graph object and a NodeDef from a GraphDef, and if
  there's an associated statistics method, calls it and returns a result. If no
  function has been registered for the particular node type, it returns an empty
  statistics object.

  Args:
    graph: A Graph object that's been set up with the node's graph.
    node: A NodeDef describing the operator.
    statistic_type: A string identifying the statistic we're interested in.

  Returns:
    An OpStats object containing information about resource usage.
  """

try:
    stats_func = _stats_registry.lookup(node.op + "," + statistic_type)
    result = stats_func(graph, node)
except LookupError:
    result = OpStats(statistic_type)
exit(result)
