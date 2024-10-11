# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Pops the given tape in the stack."""
pywrap_tfe.TFE_Py_TapeSetRemove(tape._tape)  # pylint: disable=protected-access
