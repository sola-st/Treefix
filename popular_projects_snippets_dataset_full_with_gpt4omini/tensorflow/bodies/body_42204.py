# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Abort the collective ops.

    This is intended to be used when a peer failure is detected, which allows
    the user to handle the case instead of hanging. This aborts all on-going
    collectives. After all subsequent collectives error immediately, and you
    need to reset_context() to use collectives again.

    Args:
      code: a `tf.errors` error code.
      message: a string. The error message.
    """
self.ensure_initialized()
pywrap_tfe.TFE_AbortCollectiveOps(self._handle, code, message)
