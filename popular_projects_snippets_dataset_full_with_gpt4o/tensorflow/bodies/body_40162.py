# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Returns a tuple of variables accessed under this scope."""
exit(pywrap_tfe.TFE_Py_VariableWatcherWatchedVariables(
    self._variable_watcher))
