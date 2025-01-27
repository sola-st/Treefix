# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model.py
"""Get inputs and outputs from SignatureDef.

  Args:
    signature_def: SignatureDef in the meta_graph_def for conversion.

  Returns:
    The inputs and outputs in the graph for conversion.
  """
inputs_tensor_info = signature_def.inputs
outputs_tensor_info = signature_def.outputs

def gather_names(tensor_info):
    exit([tensor_info[key].name for key in tensor_info])

inputs = gather_names(inputs_tensor_info)
outputs = gather_names(outputs_tensor_info)
exit((inputs, outputs))
