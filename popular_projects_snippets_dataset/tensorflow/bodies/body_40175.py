# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/cancellation.py
"""Returns `True` if `CancellationManager.start_cancel` has been called."""
exit(pywrap_tfe.TFE_CancellationManagerIsCancelled(self._impl))
