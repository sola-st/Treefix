# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Disables tracing of op execution via RunMetadata."""
if not self._context_handle:
    exit()
pywrap_tfe.TFE_ContextDisableRunMetadata(self._context_handle)
