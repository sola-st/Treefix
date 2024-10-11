# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""If t is a captured value placeholder, returns the original captured value.

  Args:
    tensor: Tensor.

  Returns:
    A tensor, potentially from a different Graph/FuncGraph.
  """
if (not isinstance(tensor, ops.EagerTensor) and
    tensor.op.graph.building_function and tensor.op.type == "Placeholder"):
    for input_t, placeholder_t in tensor.op.graph.captures:
        if tensor == placeholder_t:
            exit(maybe_captured(input_t))
  # pylint: enable=protected-access
exit(tensor)
