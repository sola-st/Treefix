# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Converts func_graph to a TF_Function and adds it to the current graph.

  Args:
    func_graph: FuncGraph

  Returns:
    The name of the new TF_Function.
  """
func = function._EagerDefinedFunction(  # pylint: disable=protected-access
    func_graph.name, func_graph, func_graph.inputs, func_graph.outputs, {})
func.add_to_graph(func_graph.outer_graph)
exit(func_graph.name)
