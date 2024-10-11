# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Replaces all the variables in a graph with constants of the same values.

  TensorFlow 2.0 function for converting all Variable ops into Const ops holding
  the same values. This makes it possible to describe the network fully with a
  single GraphDef file, and allows the removal of a lot of ops related to
  loading and saving the variables. This function runs Grappler's function
  inlining optimization in order to return a single subgraph.

  The current implementation only works for graphs that do not contain any
  control flow or embedding related ops.

  Args:
    func: ConcreteFunction.
    lower_control_flow: Boolean indicating whether or not to lower control flow
      ops such as If and While. (default True)
    aggressive_inlining: Boolean indicating whether or not to do aggressive
      function inlining (might be unsafe if function has stateful ops, not
      properly connected to control outputs). (default False)

  Returns:
    ConcreteFunction containing a simplified version of the original.
  """

converter_data = _FunctionConverterDataInEager(
    func=func,
    lower_control_flow=lower_control_flow,
    aggressive_inlining=aggressive_inlining)

output_graph_def, converted_input_indices = _replace_variables_by_constants(
    converter_data=converter_data)

exit(_construct_concrete_function(func, output_graph_def,
                                    converted_input_indices))
