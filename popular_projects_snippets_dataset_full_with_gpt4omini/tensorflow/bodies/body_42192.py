# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Clear errors in both local executors and remote workers.

    After receiving errors from remote workers, additional requests on the fly
    could further taint the status on the remote workers due to the async nature
    of remote execution. Calling this method block on waiting for all pending
    nodes in remote executors to finish and clear their error statuses.

    Raises:
      ValueError: if context is not initialized.
    """
if self._context_handle:
    pywrap_tfe.TFE_ContextClearExecutors(self._context_handle)
else:
    raise ValueError("Context is not initialized.")
