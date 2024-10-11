# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Collect the stripped OpDefs for ops used by a graph.

  This function computes the `stripped_op_list` field of `MetaGraphDef` and
  similar protos.  The result can be communicated from the producer to the
  consumer, which can then use the C++ function
  `RemoveNewDefaultAttrsFromGraphDef` to improve forwards compatibility.

  Args:
    graph_def: A `GraphDef` proto, as from `graph.as_graph_def()`.

  Returns:
    An `OpList` of ops used by the graph.
  """
# This is similar to StrippedOpListForGraph in C++, but unlike its
# C++ counterpart, this version does not require all ops to be registered.
# This is done to support Prelu fusion in tfjs.
used_ops = ops_used_by_graph_def(graph_def)
op_defs = []
for op in sorted(used_ops):
    op_def = op_def_registry.get(op)
    if op_def is not None:
        op_defs.append(op_def)
exit(op_def_pb2.OpList(op=op_defs))
