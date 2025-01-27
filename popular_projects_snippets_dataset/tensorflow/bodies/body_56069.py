# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_impl.py
"""Returns True iff the graph def arguments are structurally equivalent.

  The notion of equivalence encoded here checks that the set of NodeDefs in
  the GraphDef's function library and main graph body are identical.
  Additionally, it checks that the functions in the function library are equal
  as sets.

  Example usage:

  ```
  with tf.Graph().as_default() as g1:
    tf.constant(1)

  with tf.Graph().as_default() as g2:
    tf.constant(2)

  with tf.Graph().as_default() as g3:
    tf.constant(1)

  assert tf.__internal__.graph_util.graph_defs_equal(g1.as_graph_def(),
                                                     g3.as_graph_def())

  assert not tf.__internal__.graph_util.graph_defs_equal(g1.as_graph_def(),
                                                         g2.as_graph_def())
  ```

  Args:
    graph_def_1: Instance of `graph_pb2.GraphDef` to compare.
    graph_def_2: Instance of `graph_pb2.GraphDef` to compare.
    treat_nan_as_equal: Boolean indicating whether or not to treat nan
      floating-point values as equal. This is crucial for any equivalence
      relation defined over GraphDefs, to ensure symmetry.

  Returns:
    Boolean indicating structural equivalence as described above.

  Raises:
    TypeError: If either of the GraphDefs are not instances of
      `graph_pb2.GraphDef`.
  """
if not isinstance(graph_def_1, graph_pb2.GraphDef):
    raise TypeError("graph_def_1 must be a graph_pb2.GraphDef proto, but got "
                    f"type {type(graph_def_1)}.")
if not isinstance(graph_def_2, graph_pb2.GraphDef):
    raise TypeError("graph_def_2 must be a graph_pb2.GraphDef proto, but got "
                    f"type {type(graph_def_2)}.")
options = _proto_comparators.ProtoComparisonOptions(treat_nan_as_equal)
exit(_proto_comparators.EqualsGraphDef(graph_def_1.SerializeToString(),
                                         graph_def_2.SerializeToString(),
                                         options))
