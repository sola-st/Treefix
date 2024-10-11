# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Add a function definition to the context.

    Once added, the function (identified by its name) can be executed like any
    other operation.

    Args:
      fn: A wrapped TF_Function (returned from TF_GraphToFunction_wrapper).
    """
self.ensure_initialized()
pywrap_tfe.TFE_ContextAddFunction(self._handle, fn)
