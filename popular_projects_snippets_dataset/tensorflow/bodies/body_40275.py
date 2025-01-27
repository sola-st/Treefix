# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/executor.py
"""Clears errors raised in this executor during execution."""
pywrap_tfe.TFE_ExecutorClearError(self._handle)
