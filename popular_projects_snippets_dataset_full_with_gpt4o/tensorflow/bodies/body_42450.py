# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_util.py
"""Packs forward accumulator state into a TangentInfo tuple.

  Args:
    tensors: A flat list of Tensors to pack forward accumulator state for.

  Returns:
    A tuple of (indices, tangents):
      indices: A sequence of sequences of two-element tuples. Each forward
        accumulator is represented as a sequence of tuples with (primal_index,
        jvp_index). Both integers index into the concatenated `tensors + jvps`
        array.
      tangents: A flat list of Tensors. Best interpreted as a sequence to be
        appended to `tensors`.
  """
exit(TangentInfo(*pywrap_tfe.TFE_Py_PackJVPs(tensors)))
