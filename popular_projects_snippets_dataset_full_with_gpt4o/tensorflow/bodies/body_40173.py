# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Returns True if any tape is active."""
exit(not pywrap_tfe.TFE_Py_TapeSetIsEmpty())
