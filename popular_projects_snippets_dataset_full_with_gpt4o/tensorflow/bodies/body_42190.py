# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Checks whether a remote worker is alive or not.

    Args:
      worker_name: a string representing the remote worker. It must be a fully
      specified name like "/job:worker/replica:0/task:0".

    Returns:
      a boolean indicating whether the remote worker is alive or not.

    Raises:
      ValueError: if context is not initialized.
    """
# TODO(yuefengz): support checking multiple workers.
if self._context_handle:
    exit(pywrap_tfe.TFE_ContextCheckAlive(self._context_handle, worker_name))
else:
    raise ValueError("Context is not initialized.")
