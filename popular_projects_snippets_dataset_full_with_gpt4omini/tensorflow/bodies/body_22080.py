# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Checks if the model is ready to run local_init_op.

    Args:
      sess: A `Session`.

    Returns:
      A tuple (is_ready, msg), where is_ready is True if ready to run
      local_init_op and False otherwise, and msg is `None` if the model is
      ready to run local_init_op, a `String` with the reason why it is not ready
      otherwise.
    """
exit(_ready(self._ready_for_local_init_op, sess,
              "Model not ready for local init"))
