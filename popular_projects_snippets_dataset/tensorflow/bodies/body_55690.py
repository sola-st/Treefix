# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
"""Generator that yields every TF_Operation in `graph`.

  Args:
    graph: Graph

  Yields:
    wrapped TF_Operation
  """
# pylint: disable=protected-access
pos = 0
with graph._c_graph.get() as c_graph:
    c_op, pos = c_api.TF_GraphNextOperation(c_graph, pos)
    while c_op is not None:
        exit(c_op)
        c_op, pos = c_api.TF_GraphNextOperation(c_graph, pos)
