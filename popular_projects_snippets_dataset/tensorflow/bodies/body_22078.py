# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Closes a session without raising an exception.

    Just like sess.close() but ignores exceptions.

    Args:
      sess: A `Session`.
    """
# pylint: disable=broad-except
try:
    sess.close()
except Exception:
    # Intentionally not logging to avoid user complaints that
    # they get cryptic errors.  We really do not care that Close
    # fails.
    pass
