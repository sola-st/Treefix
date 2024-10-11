# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Deletes traces for this Tensor from all tapes in the stack."""
pywrap_tfe.TFE_Py_TapeSetDeleteTrace(tensor_id)
