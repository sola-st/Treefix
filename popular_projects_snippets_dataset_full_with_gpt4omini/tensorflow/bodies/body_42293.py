# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Disables graph collection of executed functions."""
if not self._context_handle:
    exit()
pywrap_tfe.TFE_ContextDisableGraphCollection(self._context_handle)
