# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils.py
"""Strips all nonessential strings from the model to reduce model size.

  We remove the following strings:
  (find strings by searching ":string" in the tensorflow lite flatbuffer schema)
  1. Model description
  2. SubGraph name
  3. Tensor names
  We retain OperatorCode custom_code and Metadata name.

  Args:
    model: The model from which to remove nonessential strings.
  """

model.description = None
for subgraph in model.subgraphs:
    subgraph.name = None
    for tensor in subgraph.tensors:
        tensor.name = None
  # We clear all signature_def structure, since without names it is useless.
model.signatureDefs = None
