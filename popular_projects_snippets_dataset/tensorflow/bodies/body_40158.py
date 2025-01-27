# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Marks this tensor to be watched by the given tape."""
pywrap_tfe.TFE_Py_TapeWatch(tape._tape, tensor)  # pylint: disable=protected-access
