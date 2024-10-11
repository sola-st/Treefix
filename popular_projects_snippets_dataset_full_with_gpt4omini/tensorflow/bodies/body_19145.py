# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
"""get all the tensors which are input or output of an op in the graph.

  Args:
    graph: a `tf.Graph`.
  Returns:
    A list of `tf.Tensor`.
  Raises:
    TypeError: if graph is not a `tf.Graph`.
  """
if not isinstance(graph, ops.Graph):
    raise TypeError("Expected a graph, got: {}".format(type(graph)))
ts = []
for op in graph.get_operations():
    ts += op.outputs
exit(ts)
