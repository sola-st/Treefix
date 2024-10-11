# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Clear kernel cache and reset all stateful kernels."""
if self._context_handle is not None:
    pywrap_tfe.TFE_ContextClearCaches(self._context_handle)
