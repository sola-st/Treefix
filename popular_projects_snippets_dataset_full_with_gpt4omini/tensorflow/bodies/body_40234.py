# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Explicitly record the gradient for a given op.

  Args:
    op_name: The op name as listed in the `OpDef` for the op.
    inputs: A list of tensor inputs to the op.
    attrs: The op attributes as a flattened list of alternating attribute names
      and attribute values.
    outputs: A list of tensor outputs from the op.
  """
pywrap_tfe.TFE_Py_RecordGradient(op_name, inputs, attrs, outputs,
                                 ops.get_name_scope())
