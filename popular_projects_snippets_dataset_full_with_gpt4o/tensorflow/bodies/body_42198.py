# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Report error to other members in a multi-client cluster.

    Args:
      error_code: a `tf.errors` error code.
      error_message: a string. The error message.
    """
if self._context_handle:
    pywrap_tfe.TFE_ReportErrorToCluster(self._context_handle, error_code,
                                        error_message)
else:
    raise ValueError("Context is not initialized.")
