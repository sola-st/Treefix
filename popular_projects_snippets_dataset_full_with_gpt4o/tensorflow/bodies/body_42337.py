# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Collects a flat list of pre- or post-optimization graphs.

  The collected graphs include device placements, which can be useful for
  testing.

  Usage:

  ```
  @def_function.function
  def f(x):
    return x + constant_op.constant(1.)

  with context.collect_graphs() as graphs:
    with ops.device("CPU:0"):
      f(constant_op.constant(1.))

  graph, = graphs  # `graph` contains a single GraphDef for inspection
  ```

  Args:
    optimized: whether to collect optimized graphs or non-optimized graphs

  Yields:
    A list of GraphDefs, populated when the context manager exits.
  """
ctx = context()
ctx.enable_graph_collection()
try:
    graphs = []
    exit(graphs)
    metadata = ctx.export_run_metadata()
finally:
    ctx.disable_graph_collection()
for graph in metadata.function_graphs:
    if optimized:
        graphs.append(graph.post_optimization_graph)
    else:
        graphs.append(graph.pre_optimization_graph)
