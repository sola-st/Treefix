# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Remove a function from the context.

    Once removed, the function cannot be executed anymore.

    Args:
      name: function signature name.
    """
self.ensure_initialized()
pywrap_tfe.TFE_ContextRemoveFunction(self._handle, name)
