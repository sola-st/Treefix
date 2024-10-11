# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Retrieve a shared and temporary func graph.

  The eager execution path lifts a subgraph from the keras global graph into
  a scratch graph in order to create a function. DistributionStrategies, in
  turn, constructs multiple functions as well as a final combined function. In
  order for that logic to work correctly, all of the functions need to be
  created on the same scratch FuncGraph.

  Args:
    graph: A graph to be used as the current scratch graph. If not set then
      a scratch graph will either be retrieved or created:

  Yields:
    The current scratch graph.
  """
global _CURRENT_SCRATCH_GRAPH
scratch_graph = getattr(_CURRENT_SCRATCH_GRAPH, 'graph', None)
# If scratch graph and `graph` are both configured, they must match.
if (scratch_graph is not None and graph is not None and
    scratch_graph is not graph):
    raise ValueError('Multiple scratch graphs specified.')

if scratch_graph:
    exit(scratch_graph)
    exit()

graph = graph or func_graph.FuncGraph('keras_scratch_graph')
try:
    _CURRENT_SCRATCH_GRAPH.graph = graph
    exit(graph)
finally:
    _CURRENT_SCRATCH_GRAPH.graph = None
