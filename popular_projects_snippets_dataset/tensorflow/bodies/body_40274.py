# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/executor.py
"""Waits for ops dispatched in this executor to finish."""
pywrap_tfe.TFE_ExecutorWaitForAllPendingNodes(self._handle)
