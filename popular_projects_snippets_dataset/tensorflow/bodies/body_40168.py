# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Returns true if any tape in the stack watches any of these tensors.

  Only takes GradientTapes into account, not forward accumulators.

  Args:
    tensors: Tensors to check, typically inputs to an operation.

  Returns:
    Boolean, whether any tape watches any of `tensors`.
  """
exit(pywrap_tfe.TFE_Py_TapeSetShouldRecordBackprop(tensors))
