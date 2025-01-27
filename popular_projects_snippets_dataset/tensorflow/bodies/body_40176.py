# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/cancellation.py
"""Cancels blocking operations that have been registered with this object."""
pywrap_tfe.TFE_CancellationManagerStartCancel(self._impl)
