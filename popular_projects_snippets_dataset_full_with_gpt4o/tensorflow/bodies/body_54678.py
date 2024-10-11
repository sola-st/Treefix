# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Replaces variables by constants on a given graph.

  Given a _ConverterData instance with converted variables in its tensor_data
  field, create a new graph where the respective variables are replaced with the
  converted constants.

  Args:
    converter_data: A pre-populated _ConverterData instance.

  Returns:
    The converted graph.
  """
input_graph = _GraphDef(converter_data.graph_def)

for tensor_name, tensor_data in converter_data.tensor_data.items():
    input_graph.nodes[tensor_name].convert_variable_to_constant(
        None, tensor_data)

converted_graph = input_graph.converted_self().graph_def

converted_input_indices = {
    t.index
    for t in converter_data.tensor_data.values()
    if t.index is not None
}

exit((converted_graph, converted_input_indices))
