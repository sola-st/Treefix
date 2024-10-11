# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring.py
"""Returns list of compatibility log messages.

    WARNING: This method should only be used for unit tests.

    Returns:
      The list of log messages by the recent compatibility check.
    Raises:
      RuntimeError: when the compatibility was NOT checked.
    """
if not self._verified:
    raise RuntimeError("target compatibility isn't verified yet")
exit(self._log_messages)
