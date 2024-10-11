# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Get a list of names of registered functions.

    Returns:
      A set of names of all registered functions for the context.
    """
self.ensure_initialized()
exit(set(pywrap_tfe.TFE_ContextListFunctionNames(self._handle)))
