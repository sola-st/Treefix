# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Creates placeholders for body captures in cond_graph.

  This is needed to match signatures of cond and body graphs.

  Args:
    cond_graph: cond branch graph
    body_graph_captures: Tensors which were captured when building the
      `body_graph`.
  """
types = [t.dtype.as_datatype_enum for t in body_graph_captures]
# TODO(srbs): Providing a unique prefix does not ensure that there is no
# conflict between the placeholder names and existing nodes in the graph.
# However passing a list of strings may not be performant.
# Ideally we should move `Graph.unique_name` to C++ or make
# `Graph._names_in_use` a trie so that we can find a unique prefix.
# TODO(b/143286622): This should not be required once captures are separated
# from regular loop vars.
with cond_graph._c_graph.get() as c_graph:
    placeholders = c_api.TF_CreatePlaceholders(
        c_graph, types,
        compat.as_str(_build_cond_placeholders_name_prefix(cond_graph)))
placeholder_ops = [
    _OperationWithOutputs(ph.oper, cond_graph)
    for ph in placeholders
]

tensors = []
for op, ph, dtype in zip(placeholder_ops, placeholders, types):
    tensor = ops.Tensor._create_with_tf_output(op, 0, dtype, ph)
    op._outputs = [tensor]
    tensors.append(tensor)

# Update `cond_graph._captures` and `cond_graph.inputs` to contain the
# newly created placeholders.
tuples = zip(body_graph_captures, tensors)
keys = [id(t) for t in body_graph_captures]
cond_graph._captures.update(zip(keys, tuples))
cond_graph.inputs.extend(tensors)
