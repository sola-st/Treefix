# Extracted from ./data/repos/tensorflow/tensorflow/tools/graph_transforms/__init__.py
"""Python wrapper for the Graph Transform Tool.

  Gives access to all graph transforms available through the command line tool.
  See documentation at https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/graph_transforms/README.md
  for full details of the options available.

  Args:
    input_graph_def: GraphDef object containing a model to be transformed.
    inputs: List of node names for the model inputs.
    outputs: List of node names for the model outputs.
    transforms: List of strings containing transform names and parameters.

  Returns:
    New GraphDef with transforms applied.
  """

input_graph_def_string = input_graph_def.SerializeToString()
inputs_string = compat.as_bytes(",".join(inputs))
outputs_string = compat.as_bytes(",".join(outputs))
transforms_string = compat.as_bytes(" ".join(transforms))
output_graph_def_string = TransformGraphWithStringInputs(
    input_graph_def_string, inputs_string, outputs_string, transforms_string)
output_graph_def = graph_pb2.GraphDef()
output_graph_def.ParseFromString(output_graph_def_string)
exit(output_graph_def)
