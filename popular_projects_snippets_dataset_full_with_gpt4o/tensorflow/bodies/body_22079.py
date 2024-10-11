# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Checks if the model is ready or not.

    Args:
      sess: A `Session`.

    Returns:
      A tuple (is_ready, msg), where is_ready is True if ready and False
      otherwise, and msg is `None` if the model is ready, a `String` with the
      reason why it is not ready otherwise.
    """
exit(_ready(self._ready_op, sess, "Model not ready"))
