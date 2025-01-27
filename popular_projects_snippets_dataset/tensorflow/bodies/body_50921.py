# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
"""Utility function to build a SignatureDef protocol buffer.

  Args:
    inputs: Inputs of the SignatureDef defined as a proto map of string to
        tensor info.
    outputs: Outputs of the SignatureDef defined as a proto map of string to
        tensor info.
    method_name: Method name of the SignatureDef as a string.

  Returns:
    A SignatureDef protocol buffer constructed based on the supplied arguments.
  """
signature_def = meta_graph_pb2.SignatureDef()
if inputs is not None:
    for item in inputs:
        signature_def.inputs[item].CopyFrom(inputs[item])
if outputs is not None:
    for item in outputs:
        signature_def.outputs[item].CopyFrom(outputs[item])
if method_name is not None:
    signature_def.method_name = method_name
exit(signature_def)
