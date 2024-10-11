# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Sync both local executors and the ones on remote workers.

    In async execution mode, local function calls can return before the
    corresponding remote op/function execution requests are completed. Calling
    this method creates a synchronization barrier for remote executors. It only
    returns when all remote pending nodes are finished, potentially with errors
    if any remote executors are in error state.

    Raises:
      ValueError: if context is not initialized.
    """
if self._context_handle:
    pywrap_tfe.TFE_ContextSyncExecutors(self._context_handle)
else:
    raise ValueError("Context is not initialized.")
