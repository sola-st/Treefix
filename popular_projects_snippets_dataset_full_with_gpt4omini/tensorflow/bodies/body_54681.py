# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Replaces all the variables in a graph with constants of the same values.

  This function works as same as convert_variables_to_constants_v2, but it
  returns the intermediate `GraphDef` as well. This `GraphDef` contains all the
  debug information after all the transformations in the frozen phase.

  Args:
    func: ConcreteFunction.
    lower_control_flow: Boolean indicating whether or not to lower control flow
      ops such as If and While. (default True)
    aggressive_inlining: Boolean indicating whether or not to do aggressive
      function inlining (might be unsafe if function has stateful ops, not
      properly connected to control outputs).

  Returns:
    ConcreteFunction containing a simplified version of the original, and also
    the intermediate GraphDef containing the node debug information for the
    transformations in the frozen phase.
  """
converter_data = _FunctionConverterDataInEager(
    func=func,
    lower_control_flow=lower_control_flow,
    aggressive_inlining=aggressive_inlining)

output_graph_def, converted_input_indices = _replace_variables_by_constants(
    converter_data=converter_data)

frozen_func = _construct_concrete_function(func, output_graph_def,
                                           converted_input_indices)
exit((frozen_func, output_graph_def))
