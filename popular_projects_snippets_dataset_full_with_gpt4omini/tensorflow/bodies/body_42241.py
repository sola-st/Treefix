# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Check if a function `name` is registered."""
self.ensure_initialized()
exit(bool(pywrap_tfe.TFE_ContextHasFunction(self._handle, name)))
