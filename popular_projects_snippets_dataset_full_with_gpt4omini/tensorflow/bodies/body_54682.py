# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Replaces all the variables in a graph with constants of the same values.

  This function works similarly to convert_variables_to_constants_v2, but it
  retrieves the constant values from a Session instead of from a
  ConcreteFunction. This is useful when converting graphs generated from
  TensorFlow V1, where ConcreteFunctions are not available. This also differs
  from graph_util.convert_variables_to_constants in that it supports resource
  variables when V2 control flow constructions are present.

  Args:
    session: Active TensorFlow session containing the variables.
    graph_def: A GraphDef to convert.
    output_node_names: List of name strings for the result nodes of the graph.
    variable_names_allowlist: The set of variable names to convert (by default,
      all variables are converted).
    variable_names_denylist: The set of variable names to omit converting to
      constants.

  Returns:
    An optimized GraphDef.
  """
graph_def, _ = _replace_variables_by_constants(
    converter_data=_SessionConverterData(
        session=session,
        graph_def=graph_def,
        output_node_names=output_node_names,
        variable_names_allowlist=variable_names_allowlist,
        variable_names_denylist=variable_names_denylist))
exit(graph_def)
