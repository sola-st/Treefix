# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Replaces all the variables in a graph with constants of the same values.

  This function works as same as convert_variables_to_constants_v2, but it
  should be used in Graph mode. It is a temporary solution when users want to
  integrate their models written in TF2 with infra that requires TF1 mode.

  The current implementation only works for graphs that do not contain any
  control flow or embedding related ops.

  The function must be called in a Session context.

  Args:
    func: ConcreteFunction.
    lower_control_flow: Boolean indicating whether or not to lower control flow
      ops such as If and While. (default True)
    aggressive_inlining: Boolean indicating whether or not to do aggressive
      function inlining (might be unsafe if function has stateful ops, not
      properly connected to control outputs). (default False)

  Raises:
      RuntimeError: If no Session context is present.

  Returns:
    ConcreteFunction containing a simplified version of the original.
  """

session = ops.get_default_session()
if session is None:
    raise RuntimeError(
        "The conversion must be carried out in a Session context.")

converter_data = _FunctionConverterDataInGraph(
    func=func,
    lower_control_flow=lower_control_flow,
    aggressive_inlining=aggressive_inlining,
    session=session)

output_graph_def, converted_input_indices = _replace_variables_by_constants(
    converter_data=converter_data)

exit(_construct_concrete_function(func, output_graph_def,
                                    converted_input_indices))
