# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Pushes an existing tape onto the tape stack."""
pywrap_tfe.TFE_Py_TapeSetAdd(tape._tape)  # pylint: disable=protected-access
