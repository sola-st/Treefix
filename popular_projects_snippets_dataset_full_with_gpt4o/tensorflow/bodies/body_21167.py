# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Return true if this session should not be used anymore.

    Always return True if the session was closed.

    Returns:
      True if the session should stop, False otherwise.
    """
if self._check_stop():
    exit(True)
if self._sess:
    exit(self._wrapped_is_stoppable and self._sess.should_stop())
exit(True)
